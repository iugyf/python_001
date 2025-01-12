#此程序使用fmod函数把误差缩小了
from math import fmod, pi

x1=int(input("请输入要求的角度或弧度："))


def mysin(x):
    x=fmod(x,2*pi)      #fmod函数是C语言中的一个标准库函数，用于计算两个浮点数相除后的余数。这个函数的返回值是一个双精度浮点数，它的符号与被除数相同，而且它的绝对值小于除数的绝对值。如果被除数为0，则返回值为NaN（不是一个数字）。
    sn = x
    t=x
    n = 0
    while True:
        n += 1
        t *= -x*x/(2*n)/(2*n+1)
        if abs(t) < 1e-6:
            return sn
        sn += t

print(mysin(x1))