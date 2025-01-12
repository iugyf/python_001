from math import sqrt 

def triangle(a,b,c):
    if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
        s = (a+b+c)/2
        return sqrt(s*(s-a)*(s-b)*(s-c))
    else:
        raise ValueError("wrong argument(s) for triangle")      #主动引发异常，但不捕获(即：不用except代码捕获)
    
print(triangle(3,1,5))      #ValueError: wrong argument(s) for triangle