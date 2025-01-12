# 3. 带有参数的被装饰函数
    # 如果被装饰的函数本身也接受参数，你需要确保装饰器能够正确处理这些参数。
    # 为此，可以在装饰器的 wrapper 函数中使用 *args 和 **kwargs 来接收任意数量的位置参数和关键字参数。

# 示例 3：带有参数的被装饰函数


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        result = func(*args, **kwargs)  # 调用原始函数并传递参数
        print("After the function is called.")
        return result
    return wrapper

# 使用装饰器
@my_decorator
def add(a, b):
    return a + b

# 调用被装饰的函数
result = add(3, 5)
print(f"Result: {result}")


# 输出：
    # Before the function is called.
    # After the function is called.
    # Result: 8

# 解释：
    # my_decorator 的 wrapper 函数使用 *args 和 **kwargs 来接收任意数量的参数，并将它们传递给原始函数 add。
    # 这样，即使 add 函数接受参数，装饰器仍然可以正常工作。