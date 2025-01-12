# 在 Python 中，装饰器可以接受参数，并将这些参数传递给被装饰的函数。为了实现这一点，你需要创建一个 装饰器工厂，
# 即一个返回装饰器的函数。这个装饰器工厂接受参数，并根据这些参数生成一个具体的装饰器。然后，这个装饰器会包装原始函数，并将参数传递给它。




########################################################################
print("########################################################################")
print("1. 带参数的装饰器的基本结构")
# 1. 带参数的装饰器的基本结构
    # 要创建一个带参数的装饰器，通常需要三层嵌套函数：
        # 最外层：装饰器工厂，接受装饰器的参数。
        # 中间层：实际的装饰器，接受被装饰的函数。
        # 最内层：包装函数（wrapper），接受被装饰函数的参数，并在调用被装饰函数时传递这些参数。

# 示例：带参数的装饰器

def repeat(num_times):  # 装饰器工厂，接受装饰器参数
    def decorator(func):  # 实际的装饰器，接受被装饰的函数
        def wrapper(*args, **kwargs):  # 包装函数，接受被装饰函数的参数
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)  # 使用带参数的装饰器
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


# 输出：
    # Hello, Alice!
    # Hello, Alice!
    # Hello, Alice!


# 2. 参数传递的详细过程
    # 让我们逐步分析上述代码中参数是如何传递的：
        # 装饰器工厂 repeat(num_times)：
        # 这个函数接受装饰器的参数 num_times，并返回一个实际的装饰器 decorator。
        # num_times 是装饰器的参数，而不是被装饰函数的参数。
        # 实际的装饰器 decorator(func)：
        # 这个函数接受被装饰的函数 func，并返回一个包装函数 wrapper。
        # func 是被装饰的函数（在这个例子中是 greet）。
        # 包装函数 wrapper(*args, **kwargs)：
        # 这个函数接受被装饰函数的参数 *args 和 **kwargs，并在调用 func 时将这些参数传递给它。
        # wrapper 是最终替换 greet 的函数，因此当你调用 greet("Alice") 时，实际上是在调用 wrapper("Alice")。
        # 调用 greet("Alice")：
        # 当你调用 greet("Alice") 时，实际上是调用了 wrapper("Alice")。
        # wrapper 会根据 num_times 的值（这里是 3），重复调用 greet("Alice") 三次。




# 3. 带参数的装饰器与函数参数的关系
    # 装饰器参数：装饰器的参数（如 num_times）是在定义装饰器时传递的，它们不会直接传递给被装饰的函数。
    # 装饰器工厂会根据这些参数生成一个具体的装饰器。
    # 函数参数：被装饰函数的参数（如 greet 函数中的 name）是在调用被装饰函数时传递的。
    # 包装函数 wrapper 会接收这些参数，并在调用被装饰函数时将它们传递给它。






########################################################################
print("########################################################################")
print("4. 更复杂的例子：传递参数给被装饰函数")
# 4. 更复杂的例子：传递参数给被装饰函数
    # 有时，你可能希望装饰器的参数能够影响被装饰函数的行为。例如，你可以传递一些配置参数，让被装饰函数根据这些参数做出不同的响应。

# 示例：传递参数给被装饰函数

def with_prefix(prefix):  # 装饰器工厂，接受装饰器参数
    def decorator(func):  # 实际的装饰器，接受被装饰的函数
        def wrapper(*args, **kwargs):  # 包装函数，接受被装饰函数的参数
            # 将 prefix 参数传递给被装饰函数
            result = func(prefix, *args, **kwargs)
            return result
        return wrapper
    return decorator

@with_prefix("Mr.")  # 使用带参数的装饰器
def greet(prefix, name):
    print(f"{prefix} {name}, how are you?")

greet("Alice")


# 输出：
    # Mr. Alice, how are you?


# 解释：
    # with_prefix("Mr.") 是装饰器工厂，它接受装饰器参数 prefix，并返回一个实际的装饰器 decorator。
    # decorator 接受被装饰的函数 greet，并返回一个包装函数 wrapper。
    # wrapper 在调用 greet 时，将 prefix 作为第一个参数传递给 greet，并将其余的参数（如 name）也传递给 greet。
    # 当你调用 greet("Alice") 时，实际上是调用了 wrapper("Alice")，而 wrapper 会将 prefix 和 name 一起传递给 greet。






########################################################################
print("########################################################################")
print("5. 使用 functools.wraps 保留元信息")
# 5. 使用 functools.wraps 保留元信息
    # 默认情况下，装饰器会替换原始函数，导致一些元信息（如函数名、文档字符串等）丢失。为了避免这种情况，
    # 你可以使用 functools.wraps 装饰器来保留原始函数的元信息。

# 示例：使用 functools.wraps


from functools import wraps

def with_prefix(prefix):
    def decorator(func):
        @wraps(func)  # 保留原始函数的元信息
        def wrapper(*args, **kwargs):
            result = func(prefix, *args, **kwargs)
            return result
        return wrapper
    return decorator

@with_prefix("Dr.")
def greet(prefix, name):
    """Greet a person with a title."""
    print(f"{prefix} {name}, how are you?")

print(greet.__name__)  # 输出: greet
print(greet.__doc__)   # 输出: Greet a person with a title.


# 解释：
    # @wraps(func) 装饰器用于保留原始函数的元信息，如函数名和文档字符串。
    # 如果不使用 @wraps，greet.__name__ 会变成 wrapper，而 greet.__doc__ 会变成 None。



# 6. 总结
    # 带参数的装饰器 需要创建一个 装饰器工厂，即一个返回装饰器的函数。装饰器工厂接受装饰器的参数，并根据这些参数生成一个具体的装饰器。
    # 装饰器参数 是在定义装饰器时传递的，它们不会直接传递给被装饰的函数。装饰器工厂会根据这些参数生成一个具体的装饰器。
    # 函数参数 是在调用被装饰函数时传递的。包装函数 wrapper 会接收这些参数，并在调用被装饰函数时将它们传递给它。
    # 你可以使用 functools.wraps 来保留原始函数的元信息，避免装饰器替换掉函数名、文档字符串等。