# 本模块实现Pi估值程序的主线程，主要建立了一个GUI类，
# 还定义了一个计算Pi值的辅助函数，队列 rqueue 用于线程间通信

import tkinter as tk                                                    # GUI库

from queue import Queue, Empty                                          # 消息队列库
from random import randrange
from P433_threading_GUI_实例_蒙特卡罗实验_01_功能模块 import Pi_est       # 自定义类


# 基于试验结果计算Pi的估值（数学方面的知识）
def pi_value(passed, total):
    return (6 / (passed / total))**0.5

rqueue = Queue()        # 消息队列

# GUI主界面， 继承自Frame类
class Pi_GUI(tk.Frame):
    def __init__(self, min_=10000, max_=20000):
        self._total = 0         # 累积试验次数
        self._passed = 0        # 累积通过次数
        self._min = min_        # 一次试验中模拟次数的下界
        self._max = max_        # ...................上界

        tk.Frame.__init__(self)                             # 窗口框架初始化
        self.master.title('monte carlo Pi estimater')       # 父窗口(即：主窗口)抬头
        self.grid()                                         # 安置本物件到父窗口

        # 有关总试验次数的变量、标签和数值显示
        self._totalVar = tk.StringVar()             # 窗口专用的控制变量：整数变量
        self._totalVar.set('0')                     
        self._total_label = tk.Label(self, text='total tests:', anchor=tk.W, width=16)
        self._total_label.grid(row=0, column=0)
        self._total_num = tk.Label(self, anchor=tk.E, width=20, textvariable=self._totalVar)
        self._total_num.grid(row=0, column=1)

        # 有关通过的试验的变量、标签和数值显示
        self._passVar = tk.StringVar()             # 窗口专用的控制变量：整数变量
        self._passVar.set('0')                     
        self._pass_label = tk.Label(self, text='passed tests:', anchor=tk.W, width=16)
        self._pass_label.grid(row=1, column=0)
        self._pass_num = tk.Label(self, anchor=tk.E, width=20, textvariable=self._passVar)
        self._pass_num.grid(row=1, column=1)

        # 有关Pi估值的变量、标签和数值显示
        self._piVar = tk.StringVar()             # 窗口专用的控制变量：整数变量
        self._piVar.set('0')                     
        self._pi_label = tk.Label(self, text='pi estimated:', anchor=tk.W, width=16)
        self._pi_label.grid(row=2, column=0)
        self._pi_num = tk.Label(self, anchor=tk.E, width=20, textvariable=self._piVar)
        self._pi_num.grid(row=2, column=1)

        # 启动一个线程试验线程的按钮
        self._compute = tk.Button(self, text='new\ntester', command=self._test, width=8)
        self._compute.grid(row=3, column=0, sticky=tk.W)

        # 连续启动三个线程试验线程的按钮
        self._compute3 = tk.Button(self, text='new 3\ntester', command=self._test3, width=8)
        self._compute3.grid(row=3, column=0, columnspan=2)
        
        # 结束按钮 
        self._finish = tk.Button(self, text='finish', width=8, command=self.master.destroy)
        self._finish.grid(row=3, column=1, sticky=tk.E)
        
        # 启动消息循环
        self.mainloop()


    # 启动一个测试线程，并收集已经得到的结果
    def _test(self):
        '''launch a tester.'''
        th = Pi_est(randrange(self._min, self._max,), rqueue)
        th.start()
        self._collect()

    # 连续启动三个测试线程，并收集已经得到的结果
    def _test3(self):
        '''launch 3 tester'''
        for i in range(3):
            th = Pi_est(randrange(self._min, self._max), rqueue)
            th.start()
        self._collect()

    # 收集结果的辅助函数
    def _collect(self):
        no_data = True
        while True:
            try:
                p, t = rqueue.get(timeout=0.01)     # timeout:等待时间，如果太短，可能初次点击按钮会无法收到消息，因为队列响应没那么快
            except Empty:
                if no_data: return
                else: break           
            self._passed += p
            self._total += t
            no_data = False
        self._totalVar.set(str(self._total))
        self._passVar.set(str(self._passed))
        self._piVar.set('{:18.16f}'.format(pi_value(self._passed, self._total)))



# 构建一个类实例，即启动程序
# Pi_GUI(20000, 50000)
if __name__ == "__main__":
    app = Pi_GUI(20000, 50000) # 创建Pi_GUI的实例
    app.mainloop()             # 调用实例的mainloop方法，进入tkinter的事件循环