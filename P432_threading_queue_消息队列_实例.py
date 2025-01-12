from threading import Thread                # 线程类
from queue import Queue, Empty              # 消息队列类，  空消息队列
from time import sleep                  
from random import random                   # 随机类

glist = []                                  # 表：用于存储消息

# 自定义类：生产者， 继承自“线程类”
class Producer(Thread):
    def __init__(self, name_, queue, n):        # 第二个参数：线程名     第三个参数：“消息队列”的实例对象       第四个参数： 消息个数
        Thread.__init__(self, name=name_)
        self._queue = queue
        self._num = n

    def run(self):                              # 开始执行本类，
        for i in range(self._num):
            sleep(0.1 * random())
            self._queue.put((self.name, i))     # 将消息存入 “消息队列”中     这里的每组消息是：线程名，序号

# 自定义类：消费者   继承自“线程类”
class Consumer(Thread):
    def __init__(self, name_, queue):
        Thread.__init__(self, name=name_)
        self._queue = queue

    def run(self):
        while True:
            try:
                glist.append(self._queue.get(timeout=0.2))   # 从“消息队列”中取消息。超过0.2秒未取到消息，就抛出异常
            except Empty:
                break                                        # 未取到消息就退出循环


q = Queue()         # 构建“消息队列”

Producer("p1", q, 10).start()   # 构建生产者线程， 线程名：“p1”, 消息队列：q,  消息个数：10个。  最后启动线程“.start()”
Producer("p2", q, 10).start()
cons = Consumer('c1', q)        # 构建消费者线程
cons.start()                    # 启动消费者线程
cons.join()                     # 让主线程等待消费者线程(cons)先结束，然后再结束主线程


print(glist)                    # 打印消费队列中的消息






##################################################################################
print('\n\n上面:使用线程等待方法join()')
print("--------------------------------------------------")
print('下面:在同一个文件中,使用字符串拼接方法.join()\n')

str_1 = ['Hello','the','whorld']
str_2 = '_fuck~~~~'.join(str_1)

print('拼接前：', str_1)
print('拼接后：',str_2)
print()