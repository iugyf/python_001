x=int(input("请输入一个数:"))

#这个递归算法非常耗时，每参数增加1，用时增长约1.6倍。参数为50就要用时1小时，参数为100时要100万年。参数为1000时系统直接提示错误（因为系统本身限制递归深度).
def fib(n):
    if n<1:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(x))