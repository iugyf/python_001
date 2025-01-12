# 闭包的生命周期
# 闭包的一个重要特性是它可以在外部函数执行完毕后仍然保持对外部函数局部变量的引用。
# 这意味着闭包可以“记住”外部函数的状态，即使外部函数已经返回。

# 示例 3：闭包的生命周期


def counter():
    count = 0  # 外部函数的局部变量

    def increment():
        nonlocal count  # 声明 count 是外部函数的局部变量
        count += 1
        return count

    return increment        # 此处返回不加括号，返回的是子函数。   若加括号，则返回子函数的计算结果。

# 创建闭包
counter_func = counter()

# 调用闭包多次
print(counter_func())  # 输出: 1
print(counter_func())  # 输出: 2
print(counter_func())  # 输出: 3




###########################################################################
# 解释：

# counter 是一个外部函数，它定义了一个局部变量 count，初始值为 0。
# increment 是一个内部函数，它使用 nonlocal 关键字声明 count 是外部函数的局部变量，并对其进行了修改。
# counter 返回 increment，因此 increment 会记住 count 的值。
# 每次调用 counter_func() 时，increment 都会更新并返回 count 的值，因此我们可以看到 count 的值逐渐增加。
# 注意：
# nonlocal 关键字用于在内部函数中修改外部函数的局部变量。如果没有 nonlocal，内部函数只能读取外部函数的局部变量，但不能修改它们。