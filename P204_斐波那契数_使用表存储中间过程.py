def fib(n):

    # if n==0:              #如果没有这句，程序输入0时，会报错，因为下面fibs[1]=1会溢出
    #     return 0

    fibs = [-1] * (n+1)     #用于存储中间计算过程，初始化全置0
    fibs[0] = 0             #初始值，用于跳出下面的递归函数
    fibs[1] = 1             #初始值，用于跳出下面的递归函数

    def fib0(k):
        if fibs[k] != -1:
            return fibs[k]
        fibs[k] = fib0(k-2) + fib0(k-1)
        return fibs[k]
    return fib0(n)

#print(fib(0))         #如果输入0会报错，因为下标溢出

x1 = int(input("请输入你要求的斐波那契数项：")) #如果输入0会报错，因为下标溢出
print(fib(x1))