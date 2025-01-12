from time import time


x1=int(input("请输入两个数:"))
x2=int(input())


#这个递归算法非常耗时，每参数增加1，用时增长约1.6倍。参数为50就要用时1小时，参数为100时要100万年。参数为1000时系统直接提示错误（因为系统本身限制递归深度).
def fib(n):
    if n<1:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)

#计算程序用时
def test_fib(x):
    t=time()
    f=fib(x)
    print("Fib[" + str(x) + "] = " +  str(f) + "     Timing:" + str(time()-t) + "s\n")
    return 

#P94_循环计算斐波那契数的用时 
def test_fibs(mm,nn):
    for k in range(mm,nn):
        test_fib(k)

test_fibs(x1,x2)