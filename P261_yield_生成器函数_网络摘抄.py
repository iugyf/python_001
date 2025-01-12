#生成器对象可以用于 for 循环，Python 会自动处理 StopIteration 异常，因此你不需要手动捕获它。

def simple_generator():
    yield 1
    yield 2
    yield 3


#================================================================
# 使用 for 循环遍历生成器   for 循环会自动调用 next() 来获取生成器的值，并在遇到 StopIteration 时停止循环。
for value in simple_generator():
    print(value)




#================================================================
print("-----------------------------------")
# 创建生成器对象
gen = simple_generator()

# 逐个获取生成器生成的值
print(next(gen))  # 输出: 1
print(next(gen))  # 输出: 2
print(next(gen))  # 输出: 3

# 再次调用 next() 会抛出 StopIteration 异常，因为生成器已经没有更多值可生成
# print(next(gen))  # 抛出 StopIteration