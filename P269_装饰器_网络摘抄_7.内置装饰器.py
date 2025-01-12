# 7. 内置装饰器
# Python 提供了一些内置的装饰器，常见的有：
    # @staticmethod：将方法标记为静态方法，不需要传递 self 参数。
    # @classmethod：将方法标记为类方法，第一个参数是类本身（通常是 cls），而不是实例。
    # @property：将方法转换为属性，允许你通过点符号访问方法的结果，而不需要调用它。通过 @property 定义的属性只能被读取，不能被直接修改。
                # 只读属性可以防止外部代码随意修改对象的内部状态，增强代码的安全性和稳定性。
    # @functools.lru_cache：为函数添加缓存功能，避免重复计算相同的结果。

# 示例 7：使用 @property 装饰器


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        """Calculate the area of the circle."""
        return 3.14159 * self._radius ** 2

# 创建 Circle 对象
circle = Circle(5)

# 访问 area 属性
print(circle.area)  # 输出: 78.53975


# 解释：
    # @property 装饰器将 area 方法转换为属性，允许你通过 circle.area 直接访问面积，而不需要调用 circle.area()。