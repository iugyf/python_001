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

    #准备好待过滤的表。     本程序是选出所有n-1以下的斐波那契数表
    def map(fun, list1):            #fun: 判断该数是否加入表中。  本程序是：选出n-1以下所有的斐波那契数，       list1:待判断表。 本程序是：从0到n-1的序列数
        new_list = []
        for x in list1:
            new_list.append(fun(x))
        print("map:",new_list)
        return new_list

    #过滤表。   本程序：返回所有能被3整除的斐波那契数
    def filter(pred, list1):            #pred:判断。  本程序：判断是否能被3整除      list1:待判断用的表。 本程序：选出的n-1以下所有的斐波那契数
        res = []
        for x in list1:
            if pred(x):
                res.append(x)
        print("filter:",res)
        return res                  
    
    #返回n-1以下能被3整除的斐波那契数之和
    return reduce(lambda x,y : x + y,       
                  filter(lambda x: x%3==0,
                         map(fib, list(range(n)))),
            0)



x1=int(input("请输入一个数："))             #1000以内的斐波那契数是前20项
print(list(range(x1)))
print("能被3整除的斐波那契数前",x1,"项之和是：",fib_sum(x1))









################################################################
print("------------------------")
print("以下网络摘抄：")
def fibonacci_sum_divisible_by_3(limit):
    a, b = 0, 1
    total_sum = 0
    
    while a <= limit:
        if a % 3 == 0:
            total_sum += a
        a, b = b, a + b
    
    return total_sum

limit = 1000
result = fibonacci_sum_divisible_by_3(limit)
print(f"1000以内能被3整除的斐波那契数之和是: {result}")