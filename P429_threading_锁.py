# 分成十个线程计算，使用共享变量，用锁互斥临界区

from threading import Thread, Lock

data_num = 10000                        # 要计算的数据个数
segment = data_num // 10                # 将数据分段，分给10个线程，每个线程计算十分之一的数据
dlist = [i for i in range(data_num)]    # 表：保存每个数据的计算结果
llock = Lock()                          # 锁
threads = []                            # 表：子线程表，保存子线程对象

# 实际计算方法
def fun(x): return x * x

# 自定义线程类
class Calc(Thread):
    def __init__(self, begin, end):
        Thread.__init__(self)
        self._begin = begin
        self._end = end

# 线程类的执行主体
    def run(self):
        for i in range(self._begin, self._end):    # 在 begin 到 end-1 的范围内计算
            x = fun(dlist[i])                       
            with llock:                            # 锁
                dlist[i] = x                       # 临界区代码  


# 10个线程：分配各自计算范围，将线程对象加入“线程表”中，并开始计算
for i in range(10):
    th = Calc(segment*i, segment*(i+1))
    threads.append(th)
    th.start()


# 等待 “线程表” 中所有线程都执行完，再执行主线程
while threads:
    tmp = threads.pop()
    tmp.join()                  # 主线程要等待 “tmp” 线程执行完，再执行。
    print('sub-thread: '+ tmp.name + ' is terminated.')


s = 0
for i in range(data_num):
    s += dlist[i]
print("summary: ", s)
print("主线程结束，程序结束。")