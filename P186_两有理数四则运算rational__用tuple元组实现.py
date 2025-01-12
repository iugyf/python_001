#P186_有理数,用元组实现，tuple

#求出最大公约数
def gcd(m,n):     
    if m%n==0:
        return n
    return gcd(n, m%n)

#将输入的有理数标准化输出
def rational(n, d):                     # n:分子   m:分母
    assert(isinstance(n, int) and       #检查输入是否为int类型，分母是否为0 
           isinstance(d, int) and 
           d!=0),"fuck,出错了"
    
    sign =1                             #符号位
    if n<0:                             #去除分子上的符号位                      
        sign = -sign    
        n = -n
    if d<0:                             #去除分母上的符号位
        sign = -sign    
        d = -d
    
    g = gcd(n,d)                        #去除分子与分母的公约数
    return sign*(n//g), d//g           #返回标准格式的有理数



#返回有理数中的分子
def num(x):         
    return x[0]

#返回有理数中的分母
def den(x):
    return x[1]






#---------------------------------------------------------------
#有理数求反
def rat_minux(x):
    return rational(-num(x), den(x))

#有理数相加
def rat_plus(x,y):
    n = num(x)*den(y)+num(y)*den(x)
    d = den(x)*den(y)
    return rational(n,d)

#有理数相减
def rat_sub(x,y):
    n = num(x)*den(y)-num(y)*den(x)
    d = den(x)*den(y)
    return rational(n,d)

#有理数相乘
def rat_times(x,y):
    n = num(x)*num(y)
    d = den(x)*den(y)
    return rational(n,d)

#有理数相除
def rat_divid(x,y):
    n = num(x)*den(y)
    d = den(x)*num(y)
    return rational(n,d)

#打印有理数
def rat_print(x):
    print(str(num(x))+'/'+str(den(x)))




#----------------------------------------------------------------
#输出
print("-------------")
rat_print(rational(int(8), int(-26)))
rat_print(rational(int(-8), int(-42)))
#rat_print(rational(int(-8), int(0)))        #这个分母为0，上面assert会报错。






#----------------------------------------------------------------
#计算有理数

print("-------------")

x1 = int(input("请输入分子："))
x2 = int(input("请输入分母："))

#第一个有理数
rational_number1 = [2]
rational_number1 = rational(x1,x2)
rat_print(rational_number1)
print("相反数为：",end=': ')
rat_print(rat_minux(rational_number1))

#第二个有理数
print("-------------")
rational_number2 = [2]
x1 = int(input("请输入第二个有理数的分子："))
x2 = int(input("请输入第二个有理数的分母："))
rational_number2 = rational(x1,x2)
rat_print(rational_number2)
print("相反数为：",end=': ')
rat_print(rat_minux(rational_number2))


#两有理数之间运算
print("-------------")
print("两式相加：",end=': ')
rat_print(rat_plus(rational_number1,rational_number2))
print("两式相减：",end=': ')
rat_print(rat_sub(rational_number1,rational_number2))
print("两式相乘：",end=': ')
rat_print(rat_times(rational_number1,rational_number2))
print("两式相除：",end=': ')
rat_print(rat_divid(rational_number1,rational_number2))