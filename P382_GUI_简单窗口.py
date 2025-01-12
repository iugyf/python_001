import tkinter as tk


# Hello 类，继承 Frame 类。     Frame: 框架类
class Hello(tk.Frame):  
    def __init__(self, name):
        """sets up the window and widgets."""   # __doc__ 文档串
        tk.Frame.__init__(self)                 # 初始化 Frame 实例
        self.master.title("first window")       # 设置窗口标题
        self.grid()                             # 安置本 Frame

        # 下面语句建立窗口中的文字对象，其第一个参数指定父对象
        self._label = tk.Label(                     
            self, text = "good morning, " + name + "!")         # 第一个参数指定父物件（这里是根框架self）
        self._label.grid()          # 安置窗口里的文本对象

Hello("beijing").mainloop()         # 启动窗口循环，接受消息并响应