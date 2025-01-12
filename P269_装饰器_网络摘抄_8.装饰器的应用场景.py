# 8. 装饰器的应用场景
# 装饰器在许多编程场景中都非常有用，尤其是在以下情况下：
    # 日志记录：可以在函数执行前后记录日志，方便调试和监控。
    # 性能计时：可以为函数添加计时功能，测量函数的执行时间。
    # 权限验证：可以在函数执行前检查用户是否有权限执行该操作。
    # 缓存结果：可以为函数添加缓存功能，避免重复计算相同的结果。
    # 重试机制：可以在函数失败时自动重试，直到成功或达到最大重试次数。

# 示例 8：性能计时装饰器


import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

# 使用性能计时装饰器
@timer
def slow_function():
    time.sleep(2)

# 调用被装饰的函数
slow_function()



# 输出：
    # slow_function took 2.0000 seconds to execute.

# 解释：
    # @timer 装饰器会在 slow_function 执行前后记录时间，并输出函数的执行时间。