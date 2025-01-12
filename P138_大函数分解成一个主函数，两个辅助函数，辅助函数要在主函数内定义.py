#P138_大函数分解成一个主函数，两个辅助函数，辅助函数要在主函数内定义

x1=int(input("请输入要求立方根的数:"))

#全局变量，与辅助函数中的变量同名    
x=10086

    #不能在全局中定义局部函数中使用的辅助函数，否则它会优先引用全局变量
    # def improve():
    #     return (2.0*guess +x/guess/guess)/3
    # def accept():
    #     return abs((tmp-guess)/guess)<1e-6

def cbrt(x):
    #只有在本函数体中定义相应的辅助函数，就不会让辅助函数优先引用全局变量，因为本来就应该优先引用本函数的局部变量。
    def improve():
        return (2.0*guess +x/guess/guess)/3
    def accept():
        return abs((tmp-guess)/guess)<1e-6
    
    if x==0.0:
        return 0.0
    guess =x
    while True:
        tmp=improve()
        if accept():
            return tmp
        guess =tmp

print("立方根是：",cbrt(x1))