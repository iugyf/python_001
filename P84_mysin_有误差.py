#此程序输入50就得出错结果。有误差，输入越大误差越大

x1=int(input("请输入要求的角度或弧度："))


def mysin(x):
    sn = x
    t=x
    n = 0
    while True:
        n += 1
        t *= -x*x/(2*n)/(2*n+1)
        if abs(t) < 1e-6:
            return sn
        sn += t

print(mysin(x1))