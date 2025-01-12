# 本文件中定义了一组模块内部使用的功能函数，
# 而后定义线程类：Pi_est, 通过计算随机数的gcd(公约数) 做Pi估值，
# 线程把 Montecarlo 试验和通过次数送入给定队列 (参数q)

from collections.abc import Callable
from threading import Thread
from random import randrange
from typing import Any, Iterable, Mapping


# 求最大公约数
def gcd(m, n):
    if m == 0:
        return n
    while n % m != 0:
        m, n = n % m, m
    return m


# 测试： 判断两个(1到2**31-1范围内)随机数是否互为素数
def pi_test():
    a = randrange(1, 2**31)
    b = randrange(1, 2**31)
    return gcd(a, b) == 1


# 蒙特卡罗测试
def montecarlo(test, num):
    passed = 0
    for i in range(num):
        if pi_test():
            passed += 1
    return (passed, num)



# 自定义线程类：构建子线程用于计算蒙特卡罗数据
class Pi_est(Thread):
    def __init__(self, num_test, q):        # q:送结果的数据队列        num_test:测试次数
        Thread.__init__(self)               # 初始化线程
        self._num = num_test
        self._queue = q

    def run(self):                          # 启动本类实例
        self._queue.put(montecarlo(pi_test, self._num))


