#此程序输入50就得出错结果。有误差，输入越大误差越大

x1=int(input("请输入要求的角度或弧度："))
def term(x,n):
    t=(-1)**n*x**(2*n+1)
    for i in range(2,2*n+2):
        t /= i
    return t

def mysin(x):
    sn = 0.0
    n = 0
    while True:
        t = term(x,n)
        if abs(t) < 1e-6:
            return sn
        sn += t
        n += 1

print(mysin(x1))