# __new__(cls, ...)  特殊方法，类方法。     默认定义是为对象建立基本空间。该方法至少需要一个cls形参。   
#                                          在创建实例时，解释器先调用该类的__new__方法，创建基本空间之后才去调用__init__方法。                                                      

# __del__(self, ...)  特殊方法，实例方法。   将在对象被销毁之前自动调用。如果某个类的对象在销毁前需要做一些操作，可以重新定义这个方法。

# __call__(self, ...) 特殊方法，实例方法。   设 x 是 C 类的对象，C类定义了这个方法， 则 x(a1,a2,a3) 相当于 x.__call__(a1,a2,a3)
#                                          支持这个方法的对象就是可调用对象



#######################################################################################################
# 本程序的其它代码(+ - * / 等等) 见：P329_class_有理数_特殊方法_加减乘除_打印字符串等.py

class Rational:
    try:

        @staticmethod
        def _gcd(m,n):
            if n == 0:
                m,n = n,m
            while m != 0:
                m,n = n % m, m
            return n
        
        def __init__(self, num, den=1):     # num:分子   den:分母
            if not (isinstance(num,int) and isinstance(den, int)):
                raise TypeError
            if den ==0:
                raise ZeroDivisionError
            sign = 1
            if num<0:
                num, sign = -num, -sign
            if den <0:
                den, sign = -den, -sign
            g = Rational._gcd(num, den)
            self._num = sign*(num//g)
            self._den = den//g

        def num(self): return self._num    
        def den(self): return self._den


        # ---------------------------------------------------------------------------------
        # # “+” 运算 
        # def __add__(self, another):
        #     den = self._den * another.den()
        #     num = (self._num * another.den() + 
        #         self._den * another.num())
        #     return Rational(num,den)
        
        
        # 修改后的__add__方法
        def __add__(self, another):
            den = self._den * another.den()
            num = (self._num * another.den() + 
                self._den * another.num())
            
            return Rational.create(num, den)

        # 类方法
        @classmethod
        def create(cls, num, den, sign=1):
            r = Rational.__new__(Rational)      # __new__方法: 直接调用这个系统自带特殊方法，默认只是创建空间，而不执行__init__()
            g = Rational._gcd(num, den)
            r._num = sign * (num//g)
            r._den = den // g
            return r
        # ---------------------------------------------------------------------------------





        # 直接输出成字符串
        def __str__(self):
            return str(self._num) + "/" + str(self._den)
        
        # 重写print()函数
        def print(self):
            print("此处是重写print()函数：",self._num, "/", self._den)

    
    except Exception as ex:
        print("类结束时捕获错误：",ex)



x = Rational(3,4)
y = Rational(4,3)

print("x:", x)   #直接输出成字符串
print("y:", y)


print("x+y=", x+y)
