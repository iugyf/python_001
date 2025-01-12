# Thread: 线程父类
# threading：线程的库文件，也是其中的类
# target: 目标函数，也就是线程要启动的函数
# .start(): 启动线程，   如果是自定义的线程类，要在类中重写run()方法，因为这是自定义线程类的真正要执行的内容。启动时依然用start方法
# args=(参数1, 参数2, ): 这是线程的参数，为防止接收参数时，解释器弄错参数数量，最好在传递参数时最后加个逗号“,”


from threading import Thread
from datetime import datetime

def myfunc(s):
    n = 0
    for i in range(1000000):
        n += i
    print("[{}]: {}".format(s, n), datetime.now(), end = "{" + s + "}\n")


# 创建线程1，并启动
Thread(target=lambda: myfunc("1")).start()

# 创建线程2，并启动
Thread(target=lambda: myfunc("2")).start()

print("main thread terminates. 最先显示，最先完成")