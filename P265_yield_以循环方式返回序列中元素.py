def circular(seq):
    i = 0
    while True:
        yield seq[i]
        i = (i + 1) % len(seq)



# 以下这种方法每次显示的都是 0
# list_1 = list(range(1008))
# for i in range(20):
#     print(next(circular(list_1)))
        

print("--------------------------------")
# 要“直接”调用生成函数才行，不能像上面的函数一样。上面的函数list_1调用的是一般函数，再用一般函数调用生成式函数，这样每次相当于新建一个新的生成式函数了。
list_1 = circular(list(range(1008)))
for i in range(20):
    print(next(list_1))


print("--------------------------------")
for i in range(20):
    print(next(circular(range(100))))       #这个也相当于每次circular都新建一个新对象，而不是继承上个对你的数据



print("--------------------------------")
for i in range(20):
    print(id(next(circular(range(100)))))       #TMD的，看不懂，这是因为next对象是同一个吗，而它调用的id不是同一个？不知道