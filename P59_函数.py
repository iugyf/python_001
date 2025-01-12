from math import sqrt
def triangle(a,b,c):
    s=(a+b+c)/2
    area=sqrt(s*(s-a)*(s-b)*(s-c))
    return area

x=triangle(6,8,11)
y=triangle(12,17,19)-triangle(4,7,9)
z=triangle(3,9,7)*4
print("area of a triangle:",x)
print("area of a triangle with a hole:",y)
print("volume of a triangle prism:",z)