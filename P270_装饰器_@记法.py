from functools import wraps
def deco(fun):
    # @wraps(fun)         # 保留原始函数的元信息
    def wrapper(*args, **kargs):
        print(fun.__name__ + " start.")
        x=fun(*args, **kargs)
        print(fun.__name__ + " end.")
        return x
    return wrapper





#没有使用@记法时
def func1(a,b):
    print(a+b)
    return a+b


#使用@记法时,显示的东西与没有@记法时的不一样
@deco
def func2(a,b,c):
    """func2的元信息：~~~~~~~~~~~~~~~"""    
    print(a+b*c)
    return a+b*c





deco_fun1 = deco(func1)
deco_fun2 = deco(func2)

print(deco_fun1(1,4))
print("--------------------------------")
print(deco_fun2(2,3,4))

print("--------------------------------")
print(deco_fun2.__name__)  # 输出: 原始函数的元信息
print(deco_fun2.__doc__)   # 输出: 原始函数的元信息,介绍文本
