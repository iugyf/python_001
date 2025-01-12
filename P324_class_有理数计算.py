class Rationa10:
    def __init__(self, num, den=1):     # __init__自动构造函数，第一个参数也是自动生成的。  后两个参数才是调用本类时传入的实参
        self.num = num
        self.den = den
    
    def plus(self, another):            # 类中每个函数的第一个参数都是self，代表本类实例的数据
        den = self.den * another.den
        num = (self.num * another.den +
               self.den * another.num)
        return Rationa10(num, den)
    
    def prt(self):
        print(str(self.num)+'/'+str(self.den))


r0 = Rationa10(1,2)
r1 = Rationa10(3,4)
x = r0.plus(r1)
x.prt()