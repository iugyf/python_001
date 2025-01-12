#生成器的状态保存

def counter(start=0):
    count = start
    while True:
        yield count
        count += 1

# 创建生成器对象
gen = counter(5)

# 逐个获取生成器生成的值
print(next(gen))  # 输出: 5
print(next(gen))  # 输出: 6
print(next(gen))  # 输出: 7