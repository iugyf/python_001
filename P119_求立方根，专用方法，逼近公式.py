y=float(input("输入要求根的数："))

def cbrt(x):
    if x==0.0:
        return 0.0
    x1=x
    while True:
        x1 = (2.0*x1 + x/x1/x1)/3
        if abs(x1**3-x)<0.001:
            return x1

print("根：", cbrt(y))