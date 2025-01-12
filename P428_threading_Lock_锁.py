from threading import Thread, Lock

num = 0
lock = Lock()

class Adder(Thread):
    def __init__(self, name_):
        Thread.__init__(self, name=name_)

    def run(self):  # 自定义线程类时，要重写这个run方法，用以执行类实例的功能
        global num  # 声明全局变量
        for i in range(10000000):
            with lock:              # 锁
                num = num + 1

th1 = Adder("Adder1")
th1.start()
th2 = Adder("Adder2")
th2.start()

th1.join()  # 主线程等待th1线程结束
th2.join()  # 同上原理

print("result:", num)


