def outer_function(x):
    def inner_function(y):
        return x + y  # 内部函数访问外部函数的参数 x
    return inner_function  # 返回内部函数

# 创建闭包
closure = outer_function(10)

# 调用闭包      当我们调用 closure(5) 时，closure 实际上是 inner_function，它仍然记得 x = 10，因此返回 10 + 5 = 15
print(closure(5))  # 输出: 15