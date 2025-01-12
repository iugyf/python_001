from math import sin,cos

def newton(f,init):
    def diff(f):
        return lambda x: (f(x+epsilon)-f(x))/epsilon
    
    def improve(x1):
        return x1 - f(x1)/df(x1)
    
    epsilon = 0.001
    df=diff(f)
    x1=init
    x2=improve(x1)
    while abs(f(x2))>=1e-6:
        x1=x2
        x2=improve(x1)

    return x2


print("A root of sin:",newton(sin,1.0))
print("A root of cos:",newton(cos,10.0))
