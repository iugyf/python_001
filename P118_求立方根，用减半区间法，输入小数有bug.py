x1=float(input("输入要求根的数："))

def cbrt(x):
    y=abs(x)
    a, b = 0.0, y
    while True:
        m=(a+b)/2
        if abs(m**3-y)<0.001:
            return -m if x<0.0 else m
        if m**3 > y:
            b = m
        else:
            a = m           #如果输入的是小数，比如0.1，则每次都会执行这里，也就是说(m**3-y)的值会越变越大
                            #另外，如果求根的数是1，结果还是浮点数

print("根：", cbrt(x1))