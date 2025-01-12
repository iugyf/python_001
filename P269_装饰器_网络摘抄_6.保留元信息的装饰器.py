# P269_装饰器_网络摘抄_5.多层装饰器.py6. 保留元信息的装饰器
    # 默认情况下，装饰器会替换原始函数，导致一些元信息（如函数名、文档字符串等）丢失。
    # 为了避免这种情况，你可以使用 functools.wraps 装饰器来保留原始函数的元信息。

# 示例 6：保留元信息的装饰器

from functools import wraps

def my_decorator(func):
    @wraps(func)  # 保留原始函数的元信息
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        result = func(*args, **kwargs)
        print("After the function is called.")
        return result
    return wrapper

# 使用装饰器
@my_decorator
def add(a, b):
    """Add two numbers."""
    return a + b

# 检查元信息
print(add.__name__)  # 输出: add
print(add.__doc__)   # 输出: Add two numbers.


# 解释：
    # @wraps(func) 装饰器用于保留原始函数的元信息，如函数名和文档字符串。
    # 如果不使用 @wraps，add.__name__ 会变成 wrapper，而 add.__doc__ 会变成 None。