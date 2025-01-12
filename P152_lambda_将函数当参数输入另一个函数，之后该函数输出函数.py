# lambda 参数 : 函数体      返回：函数体的计算结果

from math import sin, cos, pi

epsilon = 0.01

def diff(f):
    return lambda x : (f(x + epsilon)-f(x))/epsilon

print("diff(sin(0.0) = ",  diff(sin)(0.0))      # 这里 "sin" 被传入diff的"f"中， 后面的(0.0)被传入"x"中，作lambda的参数。
print("diff(sin(pi/2) = ",  diff(sin)(pi/2))
print("diff(sin(pi) = ",  diff(sin)(pi))

def cube(x):
    return x*x*x

print("diff(cube)(1.0) =", diff(cube)(1.0))
print("diff(cube)(10.0) =", diff(cube)(10.0))