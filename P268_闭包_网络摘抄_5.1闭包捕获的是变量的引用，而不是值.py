# 5. 闭包的注意事项

# 5.1 闭包捕获的是变量的引用，而不是值
# 闭包捕获的是变量的引用，而不是变量的值。因此，如果外部函数的局部变量在闭包创建后发生了变化，闭包也会反映这些变化。

# 示例 7：闭包捕获的是引用 

def create_multipliers():
    multipliers = []
    for i in range(5):      #循环创建闭包：5个

        def multiplier(x):      
            return x * i  # i 是自由变量
        
        multipliers.append(multiplier)      # multiplier[0]:  lambda x: x*i   
                                            # multiplier[1]:  lambda x: x*i   
                                            # multiplier[2]:  lambda x: x*i   
                                            # multiplier[3]:  lambda x: x*i   
                                            # multiplier[4]:  lambda x: x*i
                                            # 可惜最后 “i” 都等于循环 5 次后的结果：4   

        print("id:",id(multipliers[i]))

    return multipliers

# 创建多个闭包
functions = create_multipliers()

# 调用闭包
for f in functions:
    print(f(2))



# 解释：

# create_multipliers 创建了 5 个闭包，每个闭包都捕获了同一个变量 i 的引用，而不是它的值。
# 当 for 循环结束时，i 的最终值是 4，因此所有闭包都返回 2 * 4 = 8。
# 这并不是我们期望的结果，因为我们希望每个闭包捕获不同的 i 值。
    




####################################################################
####################################################################
print("----------------------------------------------")
# 解决方法：
# 要解决这个问题，可以使用默认参数来捕获当前的 i 值，而不是引用。

 
def create_multipliers():
    multipliers = []
    for i in range(5):
        def multiplier(x, i=i):  # 使用默认参数捕获当前的 i 值
            return x * i
        multipliers.append(multiplier)
        print(id(multipliers[i]))
    return multipliers

# 创建多个闭包
functions = create_multipliers()

# 调用闭包
for f in functions:
    print(f(2))


# 解释：
# 通过将 i 作为默认参数传递给 multiplier，我们确保每个闭包捕获的是当前的 i 值，而不是引用。