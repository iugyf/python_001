
#框架：将会被不同主函数调用， 即：可“重用”的函数
def appr_method(x,improve,accept):
    if x==0.0:
        return 0.0
    x1=x
    while True:
        x2=improve(x,x1)    #improve:调用不同主函数中的辅助函数
        if accept(x1,x2):   #accept:调用不同主函数中的辅助函数
            return x2
        x1=x2



#主函数：求立方根
def cbrt(x):
    def cb_improve(x,x1):           #辅助函数：用于不断逼近所求的值
        return (2.0*x1+x/x1/x1)/3
    def accept(x1,x2):              #辅助函数：用于确认是否为所求的值
        return abs((x2-x1)/x1)<1e-6
    
    return appr_method(x,cb_improve,accept)     #调用框架，注意：appr_method的参数cb_improve与accept，它们本身不带参数，
                                                #               也就是说它们是将自身标识传递给appr_method，而不是将它们计算后的值传递给appr_method


#主函数：求平方根
def sqrt(x):
    def sq_improve(x,x1):     #辅助函数      
        return (x1+x/x1)/2
    def accept(x1,x2):        #辅助函数     
        return abs((x2-x1)/x1)<1e-8
    
    return appr_method(x,sq_improve,accept) #调用框架appr_method


x=int(input("请输入要求立方根与平方根的数："))
print(x,"的立方根是：",cbrt(x))
print(x,"的平方根是：",sqrt(x))