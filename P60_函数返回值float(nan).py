#P60_函数返回值float(nan)表示得到的不是一个float能表示的值
from math import sqrt

a=1
b=1
c=4

def triangle(a,b,c):
    if a>0 and b>0 and c>0 and a+b>c and b+c>a and a+c>b:
        s=(a+b+c)/2
        return sqrt(s*(s-a)*(s-b)*(s-c))
    else:
        return float("nan")
    
print(triangle(a,b,c))