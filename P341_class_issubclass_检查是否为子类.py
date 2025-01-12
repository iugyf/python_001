class MyStr(str):   # MyStr是子类（或派生类），str是父类（或基类）
    pass

s = MyStr(1234)
print(issubclass(MyStr, str))   # 判断 MyStr 是否为 str 的子类
print(isinstance(s, MyStr))
print(isinstance(s, str))



# 颠倒一下顺序
print("------------------------------------")
print(issubclass(str, MyStr))   # 判断 str 是否为 MyStr 的子类
# print(isinstance(MyStr, s))   # 直接报错
# print(isinstance(str, s))  # 直接报错



# object 是所有类的父类(无论是间接还是直接)
print("------------------------------------")
print("object 是所有类的父类(无论是间接还是直接)")
print(issubclass(MyStr, object))
print(issubclass(str, object))
print(issubclass(int, object))
print(issubclass(float, object))
print(issubclass(bool, object))