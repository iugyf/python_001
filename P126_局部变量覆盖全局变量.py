x=1

def fun2():
    y=x
   # x=2   #只要把这句注释掉，就不会产生局部变量先使用后赋值的情况，就不会报错。因为x就会使用全局变量
    return x+y

print(fun2(),x)