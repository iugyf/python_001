# 2. 带参数的装饰器
    # 有时，你可能希望装饰器能够接受参数，以便根据不同的参数来调整其行为。为了实现这一点，你可以创建一个“装饰器工厂”——即一个返回装饰器的函数。

# 示例 2：带参数的装饰器


def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# 使用带参数的装饰器
@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

# 调用被装饰的函数
greet("Alice")



# 输出：
    # Hello, Alice!
    # Hello, Alice!
    # Hello, Alice!

# 解释：
    # repeat 是一个装饰器工厂，它接受一个参数 num_times，并返回一个实际的装饰器 decorator。
    # decorator 接受一个函数 func 作为参数，并返回一个新的函数 wrapper。
    # wrapper 在调用 func 时会重复执行 num_times 次。
    # @repeat(3) 语法糖表示将 greet 函数传递给 repeat(3)，并用返回的 wrapper 替换 greet。
    # 当我们调用 greet("Alice") 时，wrapper 会重复调用 greet 三次。