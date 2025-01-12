x=3
y=5
def f1(x):
    def g(v):
        global y    #全局变量
        nonlocal z  #外围函数变量
        u=v+x
        z=u+y
        y=z*4
    g(x+1)
    z=z+y
    return z+1

def f2(x):
    z=x+y
    f1(z*x)
    return z+y

w=f2(1)
print(w)