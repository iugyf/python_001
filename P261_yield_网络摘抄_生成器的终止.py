def finite_generator():
    yield 1
    yield 2
    yield 3
    return "Done"  # 生成器终止

# 创建生成器对象
gen = finite_generator()

# 逐个获取生成器生成的值
print(next(gen))  # 输出: 1
print(next(gen))  # 输出: 2
print(next(gen))  # 输出: 3

# 再次调用 next() 会抛出 StopIteration 异常
try:
    print(next(gen))
except StopIteration as e:
    print(f"生成器已终止: {e.value}")  # 输出: 生成器已终止: Done