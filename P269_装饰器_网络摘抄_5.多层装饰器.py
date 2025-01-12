# 5. 多层装饰器
    # 你可以为同一个函数应用多个装饰器。Python 会从最内层的装饰器开始向外层依次应用每个装饰器。

# 示例 5：多层装饰器


def decorator_one(func):
    def wrapper():
        print("Decorator one before")
        func()
        print("Decorator one after")
    return wrapper

def decorator_two(func):
    def wrapper():
        print("Decorator two before")
        func()
        print("Decorator two after")
    return wrapper

# 使用多层装饰器
@decorator_one      # 外层装饰器，外层装饰器会先调用内层装饰器
@decorator_two      # 内层装饰器，最后内层装饰器才会调用下面的say_hello函数
def say_hello():
    print("Hello, world!")

# 调用被装饰的函数
say_hello()


# 输出：
    # Decorator one before
    # Decorator two before
    # Hello, world!
    # Decorator two after
    # Decorator one after

# 解释：
    # @decorator_one 和 @decorator_two 是两个不同的装饰器。
    # Python 会先应用 @decorator_two，再应用 @decorator_one。
    # 因此，say_hello 实际上被包装成了 decorator_one(decorator_two(say_hello))，所以输出顺序是从外到内的。