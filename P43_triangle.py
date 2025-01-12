from math import sqrt
#输入三条边长，求出三角形面积

a=float(input("Length of edge a:"))
b=float(input("Length of edge b:"))
c=float(input("Length of edge c:"))

s = (a+b+c)/2
area = sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle:",area)