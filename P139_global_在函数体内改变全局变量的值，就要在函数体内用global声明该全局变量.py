x1=int(input("请输入要求立方根的数:"))

#定义全局变量,用于计数：计算辅助函数运行总次数  
count = 0

def cbrt(x):

    global count        #要在本函数体内改变全局变量的值，就要用"global"声明它，注意：声明不是定义，定义要在全局中定义

    #只有在本函数体中定义相应的辅助函数，就不会让辅助函数优先引用全局变量，因为本来就应该优先引用本函数的局部变量。
    def improve():
        global count
        count +=1       #改变全局变量的值
        return (2.0*guess +x/guess/guess)/3
    def accept():
        global count
        count +=1
        return abs((tmp-guess)/guess)<1e-6
    
    count = 1
    if x==0.0:
        return 0.0
    guess =x
    while True:
        tmp=improve()
        if accept():
            return tmp
        guess =tmp

print("立方根是：", cbrt(x1), "辅助函数运行次数：",count)

#另外：内嵌函数修改外围上一层函数的变量时，要先用"nonlocal"声明，类似"global"的用法。