#P208_.P207_斐波那契数_计算前n个能被3整除的契数的和,使用内置函数map与filter实现

def fib_sum(n):

    #计算斐波那契数，用表存储中间过程，见书P204页
    def fib(n):
        
        if n == 0:
            return 0
        
        fibs = [-1] * (n+1)     #用于存储中间计算过程，初始化全置0
        fibs[0] = 0             #初始值，用于跳出下面的递归函数
        fibs[1] = 1             #初始值，用于跳出下面的递归函数

        def fib0(k):
            if fibs[k] != -1:
                return fibs[k]
            fibs[k] = fib0(k-2) + fib0(k-1)
            return fibs[k]
        
        return fib0(n)




    #主程序框架
    def reduce(fun, list1, init):   
        acc = init                   #init:初始值：0
        for x in list1:              #过滤后的斐波那契数表，即此表中的数都能被3整除
            acc = fun(acc,x)         #fun:将两数相加,即：acc+x
        return acc
    


    return reduce(lambda x,y:x+y,
                  filter(lambda x: x%3==0,              #使用内置函数map与filter
                         map(fib,list(range(n)))),
                         0)


x1=int(input("请输入一个数："))             #1000以内的斐波那契数是前20项
print(list(range(x1)))
print("能被3整除的斐波那契数前",x1,"项之和是：",fib_sum(x1))
