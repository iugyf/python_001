fs = frozenset(n**2 for n in range(-20,20))     #frozenset:不可变量的集合
print(fs)       #输出顺序是集合内部顺序，非输入顺序


print("-----------------------")
s1 = {x*y for x in range(10) for y in range(10) if x*3 < y**2}      #for循环从左到右，跟在for后面的if语句，就是与前面for配套的
print(s1)


print("-----------------------")
#上面的s1也可以写成下面
s=set()
for x in range(10):
    for y in range(10):
        if x*3 < y**2:
            s.add(x*y)
print(s)