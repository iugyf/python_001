y=float(input("输入要求根的数："))

def cbrt(x):
    if x==0.0:
        return 0.0
    x1=x
    while True:
        x2 = (2.0*x1 + x/x1/x1)/3           #本程序有错误，输入27会死循环，不知道哪里错了，也没空去查，主要是学python语法的
        if abs((x2-x1)/x1)<0.001:
            return x2
        X1=x2

print("根：", cbrt(y))