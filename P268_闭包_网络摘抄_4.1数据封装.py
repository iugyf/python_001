# 4. 闭包的应用场景
# 闭包在许多编程场景中都非常有用，尤其是在以下情况下：

# 4.1 数据封装与隐藏
# 闭包可以用来封装和隐藏数据，避免外部直接访问或修改某些变量。通过闭包，你可以创建只在特定范围内可见的变量，从而实现更好的封装性。

# 示例 4：数据封装


def create_private_counter():
    count = 0  # 私有变量

    def get_count():
        return count

    def set_count(value):
        nonlocal count
        count = value

    return get_count, set_count

# 创建闭包
get_count, set_count = create_private_counter()

# 使用闭包访问和修改私有变量
print(get_count())  # 输出: 0
set_count(10)
print(get_count())  # 输出: 10



#####################################################################33
# 解释：

# create_private_counter 创建了两个闭包 get_count 和 set_count，它们可以访问和修改外部函数的局部变量 count。
# count 是一个私有变量，外部无法直接访问它，只能通过 get_count 和 set_count 来获取和修改它的值。