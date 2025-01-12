#生成器表达式,非yield形式，一般的常用生成器

# 生成器表达式
gen = (x * x for x in range(5))

# 逐个获取生成器生成的值
for value in gen:
    print(value)