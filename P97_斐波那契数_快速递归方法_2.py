from time import time

x=int(input("请输入一个数:"))

#快速递归的方法，虽然这个方法很快，但递归函数系统已超过1000深度，经过实测，本机正好卡在20577次循环！！！    
def fib(n):
    f1,f2 = 0,1
    for k in range(n):
        f1,f2 = f2, f2+f1
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
