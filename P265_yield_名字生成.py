def id_gen(s):
    count = 0
    while True:
        yield str(s) + "_" + str(count)
        count += 1

str_1 = "fuck"

id_1 = id_gen(str_1)
for i in range(3):
    print(next(id_1))


print("------------------------------------")
print("如以下方式编程，将每次新建一个新的生成式函数")
for i in range(3):
    print(next(id_gen(str_1)))