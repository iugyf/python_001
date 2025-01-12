# 4.3 装饰器
# 闭包是实现装饰器的基础。装饰器是一种用于修改或增强函数行为的高级功能，而闭包可以让装饰器记住原始函数的参数和返回值。
# 
# 示例 6：装饰器


def my_decorator(func):
    def wrapper(*args, **kwargs):       # 第一个参数是表， 即：通过拆分表（或元组）对象的方法，给函数提供多个实参。       
                                        # 第二个参数是字典， 即：通过拆分字典的方式为函数提供一组关键字(字典的关键字字段)实参
        print("Before the function is called.")
        # result = func(*args, **kwargs)      # 本程序中，第二个参数可省略
        result = func(*args)
        print("After the function is called.")
        return result
    return wrapper      #返回不带括号，就是返回子函数本身，可将这个子函数赋值给其它对象。 如果加了括号，返回的是子函数的计算结果。

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

# 调用被装饰的函数
say_hello("Alice")
print("--------------------------------")
print(say_hello("alice"))


####################################################################
# 输出：

# 深色版本
# Before the function is called.
# Hello, Alice!
# After the function is called.
# 解释：

# my_decorator 是一个装饰器函数，它接受一个函数 func 作为参数，并返回一个闭包 wrapper。
# wrapper 在调用 func 之前和之后打印一些消息，从而增强了 func 的行为。
# @my_decorator 语法糖表示将 say_hello 函数传递给 my_decorator，并用返回的 wrapper 替换 say_hello。



