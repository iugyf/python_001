# 4. 类装饰器
    # 除了函数装饰器，Python 还支持 类装饰器。类装饰器可以用来装饰类，通常用于修改类的行为或添加类级别的功能。



# 示例 4：类装饰器

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__}")
        return self.func(*args, **kwargs)

# 使用类装饰器
@CountCalls
def say_hello():
    print("Hello, world!")

# 调用被装饰的函数
say_hello()
say_hello()


# 输出：
    # Call 1 of say_hello
    # Hello, world!
    # Call 2 of say_hello
    # Hello, world!

# 解释：
    # CountCalls 是一个类装饰器，它接受一个函数 func 作为参数，并将其存储在实例变量 self.func 中。
    # __call__ 方法使类实例可以像函数一样被调用。每次调用 say_hello() 时，实际上是在调用 CountCalls 实例的 __call__ 方法。
    # __call__ 方法会增加 num_calls 计数器，并打印调用次数，然后调用原始函数 say_hello。