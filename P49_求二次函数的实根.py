from math import sqrt

print("Program for root(s) of quadratic equetions.")
a=float(input("coefficient of x**2:"))
b=float(input("coefficient of x:"))
c=float(input("constant:"))

d = b**2-4*a*c
if d>0:
    tmp=sqrt(d)
    print("Two roots:",(-b + tmp)/2/a,(-b-tmp)/2/a)
elif d==0:
    print("one root:",-b/2/a)
else:
    print("No real root")