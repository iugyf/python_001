from functools import wraps



def deco(fun):
    # @wraps(fun)         # 保留原始函数的元信息
    def wrapper(*args, **kargs):
        print(fun.__name__ + " start.")
        x=fun(*args, **kargs)
        print(fun.__name__ + " end.")
        return x
    return wrapper


def decodeco(fun):
    def wrapper(*args, **kwargs):
        print(fun.__name__ + " ......")
        x = fun(*args, **kwargs)    #因为定义装饰器的时候是定义嵌套装饰器，本函数decodeco是外层装饰器，所以这里的"fun"是调用内层装饰器deco
        print(fun.__name__ + "------")
        return x
    return wrapper


@decodeco           # 外层装饰器
@deco               # 内层装饰器
def func4(a,b,c,d,e):
    print(a+b*c-d+e)
    return a+b*c-d+e


func4(1,2,3,4,5)