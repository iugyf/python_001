x1=float(input("输入要求根的数："))

def cbrt(x):
    y=abs(x)

    #修复如果输入值为小数就死循环的bug
    if y >= 1:
        a,b = 1.0 , y
    else:
        a,b = y, 1.0

    while True:
        m=(a+b)/2
        if abs(m**3-y)<0.001:
            return -m if x<0.0 else m
        if m**3 > y:
            b = m
        else:
            a = m           

print("根：", cbrt(x1))