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

        #def num(): return self._num        # 在定义的时候需要参数，但在类外调用的时候，不需要输入参数，因为self是类实例调用时自已自动的加上的参数
        def num(self): return self._num    
        def den(self): return self._den

        # 特殊方法名：
            # +: __add__ 
            # -: __truediv__ 
            # *: __mul__
            # /, __sub__
            # >, __gt__
            # <, __lt__
            # ==: __eq__ 
            # !=: __ne__
            # >=, __ge__
            # <=, __le__
            # //: __floordiv__：整除
            # %: __mod__
            # str: __str__: 转换成字符串

        # “+” 运算 
        def __add__(self, another):
            den = self._den * another.den()
            num = (self._num * another.den() + 
                self._den * another.num())
            return Rational(num,den)
        
        # “-” 运算 
        def __sub__(self, another):
            den = self._den * another.den()
            num = (self._num * another.den() -
                self._den * another.num())
            return Rational(num, den)

        # “*” 运算
        def __mul__(self, another):
            return Rational(self._num * another.num(),
                            self._den * another.den())

        # "//" 整除
        def __floordiv__(self, another):
            if another.num() == 0:
                raise ZeroDivisionError
            return Rational(self._num * another.den(),
                            self._den * another.num())

        # "/" 除
        def __truediv__(self, another):
            print("\n此类只做整除运算，不做浮点运算")
            return None
            
        # "%" 取模
        def __mod__(self, another):
            if another.num() == 0:
                raise ZeroDivisionError
            
            # 将两个实例的分子分母的有理数形式计算出来，即： “分子/分母”
            num = self._num * another.den()
            den = self._den * another.num()

            # 算出有理数的正负号
            sign = 1
            if num<0:
                num, sign = -num, -sign
            if den <0:
                den, sign = -den, -sign

            #求出分子与分母的最大公约数
            g = Rational._gcd(num, den)

            #化简
            num = sign*(num//g)
            den = den//g

            # 最终算出分子的余数
            num = num % den     
            
            return Rational(num, den)

        # "==" 相等比较
        def __eq__(self, another):
            return (self._num == another.num() and
                    self._den == another.den())

        # "!=" 不等比较
        def __no__(self, another):
            return (self._num != another.num() or
                    self._den != another.den())

        # "<" 小于比较
        def __lt__(self, another):
            return(self._num * another.den() <
                self._den * another.num())

        # ">" 大于比较
        def __gt__(self, another):
            return(self._num * another.den() >
                self._den * another.num())
        
        # ">=" 大等于比较
        def __ge__(self, another):
            return ((self._num * another.den() > self._den * another.num()) or      # ">"
                (self._num == another.num() and self._den == another.den()))     # "=="
    
        # "<=" 小等于比较
        def __le__(self, another):
            return (Rational.__lt__(self,another) or      # "<"     这里调用__lt__前面加Rational是同一类下的方法，并不是本实例下的方法，如果本实例下的方法不同于Rational类下的方法（即使在同一类下，不同实例的同名方法也会被改写），会出错
                self.__eq__(self,another))     # "=="                             前面加self是调用同一实例下的方法。
    
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

print("x:", x.num(), x.den())
x.print()       # 重写print()函数
print("--------------------------------")
print("x:", x)   #直接输出成字符串
print("y:", y)


print("x+y=", x+y)
print("x-y=", x-y)
print("x*y=", x*y)
print("x//y=", x//y)
print("x/y=", x/y)      # 无计算，直接返回None
print("x%y=", x%y)
print("x==y:", x==y)
print("x!=y:", x!=y)
print("x>y:", x>y)
print("x<y:", x<y)
print("x>=y:", x>=y)
print("x<=y:", x<=y)
