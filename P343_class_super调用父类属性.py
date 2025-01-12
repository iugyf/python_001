class C1:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def m1(self):
        print(self._x, self._y)
    
class C2(C1):       # C2 继承 C1
    def __init__(self, x, y):
        C1.__init__(self, x, y)
        self._x = x
        self._y = y
    
    def m1(self):
        super().m1()
        print("some special service.")
    
x = C2(3,4)
x.m1()



# ###################################################################
# # 以下是原书代码，本来就有错。
# class C1:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
    
#     def m1(self):
#         print(self._x, self._y)
    
# class C2(C1):       # C2 继承 C1

#     def m1(self):
#         super().m1()
#         print("some special service.")
    
# x = C2()        # 这里会报错，C2调用C1的初始化函数时，需要两个参数，C2未传入参数
# x.m1()