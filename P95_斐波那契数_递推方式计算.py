from time import time


x=int(input("请输入一个数:"))

#递推方式计算斐波那契数
def fib(n):
    if n<0:
        return 0
    
    f1,f2=0,1        #这里是按从左到右的顺序赋值
    print(f1,f2)   
    
    k=0
    while k<n:
        f1 , f2 = f2, f2+f1
        print(f1,f2)        #这里是按从左到右的顺序赋值
        k+=1
    return f1



#计算程序用时
def test_fib(x):
    t=time()
    f=fib(x)
    #print("Fib[" + str(x) + "] = " , f , "Timing:" + str(time()-t) + "s\n")
    #print("Fib[" , str(x) , "] = " , f , "Timing:" , str(time()-t) , "s\n")         #逗号默认会在字符两边附加空格
    #print("Fib[" + str(x) + "] = " + f + "Timing:" + str(time()-t) + "s\n")        #TypeError: can only concatenate str (not "int") to str
    str_ret = str("Fib[" + str(x) + "] = " +  str(f) + "     Timing:" + str(time()-t) + "s\n")
    return str_ret



print(test_fib(x))      

#这个程序的递推计算，直到100000才报错，比前几个递归函数厉害，而且计算的非常快。
