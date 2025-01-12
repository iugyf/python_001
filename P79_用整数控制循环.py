from math import sin, cos

value=0.0
for n in range(100):     #用整数控制循环：浮点数是近似值
    x=n*0.03
    value += sin(x*x+1)*cos(x)*0.03

print(value,x)