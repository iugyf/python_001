# 闭包与自由变量
# 在闭包中，内部函数可以访问的外部函数的局部变量称为自由变量。自由变量是指那些不在当前函数的作用域内定义，但在外部作用域中定义的变量。

# 示例 2：闭包与自由变量



def make_multiplier(factor):
    def multiply(x):
        return x * factor  # factor 是自由变量
    return multiply

# 创建两个不同的闭包
double = make_multiplier(2)
triple = make_multiplier(3)

# 调用闭包
print(double(5))  # 输出: 10
print(triple(5))  # 输出: 15


####################################################################3
# 解释：

# make_multiplier 是一个外部函数，它接受一个参数 factor。
# multiply 是一个内部函数，它接受一个参数 x，并且可以访问外部函数的参数 factor。
# make_multiplier 返回 multiply，因此 multiply 会记住 factor 的值。
# 我们创建了两个不同的闭包 double 和 triple，它们分别将 factor 设置为 2 和 3。
# 当我们调用 double(5) 时，multiply 记住了 factor = 2，因此返回 5 * 2 = 10。
# 当我们调用 triple(5) 时，multiply 记住了 factor = 3，因此返回 5 * 3 = 15。