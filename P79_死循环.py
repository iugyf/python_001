from math import sin, cos

x=0.0
value=0.0
while x != 3.0:     #死循环：浮点数是近似值
    value +=sin(x*x+1)*cos(x)*0.03
    x+=0.03

print(value,x)