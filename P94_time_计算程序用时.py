from time import time


x=int(input("请输入一个数:"))

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
    print("Fib[" + str(x) + "] = " , f , "Timing:" + str(time()-t) + "s\n")
    print("Fib[" , str(x) , "] = " , f , "Timing:" , str(time()-t) , "s\n")         #逗号默认会在字符两边附加空格
    #print("Fib[" + str(x) + "] = " + f + "Timing:" + str(time()-t) + "s\n")        #TypeError: can only concatenate str (not "int") to str
    str_ret = str("Fib[" + str(x) + "] = " +  str(f) + "     Timing:" + str(time()-t) + "s\n")
    return str_ret

print(test_fib(x))