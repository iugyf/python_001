# 装饰器（Decorator）的概念
    # 装饰器是 Python 中一种非常强大的工具，它允许你在不修改原始函数代码的情况下，动态地为函数添加新的功能。
    # 装饰器本质上是一个高阶函数，它接受一个函数作为参数，并返回一个新的函数或可调用对象。
    # 通过装饰器，你可以在函数执行前后添加额外的逻辑，或者修改函数的行为。

# 装饰器的核心思想：
    # 不修改原始函数的代码：装饰器不会改变原始函数的定义，而是通过包装的方式为其添加新功能。
    # 可复用性：装饰器可以应用于多个函数，因此它是实现代码复用的好方法。
    # 语法糖：Python 提供了 @decorator 语法糖，使得使用装饰器更加简洁和直观。


#######################################################################################3
# 1. 装饰器的基本结构

# 示例 1：简单的装饰器
def my_decorator(func):     #装饰器不会改变原始函数的定义，而是通过包装的方式为其添加新功能。   本程序此处添加：func函数参数
    def wrapper():
        print("Before the function is called.")
        func()  # 调用原始函数
        print("After the function is called.")
    return wrapper

# 使用装饰器
@my_decorator
def say_hello():
    print("Hello, world!")

# 调用被装饰的函数
say_hello()



# 输出：
    # Before the function is called.
    # Hello, world!
    # After the function is called.


#######################################################################################3
# 解释：
    # my_decorator 是一个装饰器函数，它接受一个函数 func 作为参数，并返回一个新的函数 wrapper。
    # wrapper 在调用 func 之前和之后打印一些消息，从而增强了 func 的行为。
    # @my_decorator 语法糖表示将 say_hello 函数传递给 my_decorator，并用返回的 wrapper 替换 say_hello。
    # 当我们调用 say_hello() 时，实际上是调用了 wrapper()，它在执行 say_hello 之前和之后打印了额外的消息。