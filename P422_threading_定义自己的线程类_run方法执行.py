from threading import Thread
from time import sleep

# MyThread类，继承自Thread类
class MyThread(Thread):
    num = 1
    def __init__(self):
        Thread.__init__(self, name='sub-thread-'+str(MyThread.num))
        MyThread.num += 1
    
    def run(self):      # 自定义线程类，执行时的活动由方法run定义，所以要覆盖父类(即:Thread)同名方法
        print('{} is running.'.format(self.name))
        sleep(1.0)
        self.prt()

    def prt(self):
        print('{} is running.'.format(self.name))


MyThread().start()
MyThread().start()
print('the man thread terminates.')

# 这个程序有问题，如果主程序“先”执行完的话，那子线程就无法创建，会报错。