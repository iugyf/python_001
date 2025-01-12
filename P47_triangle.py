from math import sqrt
#输入三条边长，求出三角形面积

a=float(input("Length of edge a:"))
b=float(input("Length of edge b:"))
c=float(input("Length of edge c:"))

#判断输入数据是否合法有效
if a>0 and b>0 and c>0 and \
   a+b>c and b+c>a and a+c>b:
    s= (a+b+c)/2
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of the triangle:",area)
else:
    print(a,b,c,"do not form a triangle!")