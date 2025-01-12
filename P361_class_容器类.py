class Box:
    def __init__(self, elems=[]):
        self._elems = list(elems)   # 将参数elems变成表

    # len方法
    def __len__(self):
        return len(self._elems)
    
    # 返回表下标对应的值， item：下标
    def __getitem__(self, ind):
        return self._elems[ind] + '  __getitem__方法'
    
    # 返回表下标对应的值， item：下标
    def __iter__(self): # 定义一个生成器函数
        for x in self._elems:
            yield x + ' __iter__方法'
    
    # 设置表下标对应的值， ind：下标   value：对应的值    
    def __setitem__(self, ind, value):
        self._elems[ind] = value

    # 表尾添加新元素
    def append(self, value):
        self._elems.append(value)
    
    # 判断item是否在表中
    def __contains__(self, item):
        return item in self._elems

    # 设置直接输出实例的信息
    def __str__(self):
        return "Box:" + str(self._elems)






################################################################################################
x1 = "abcdefghijklmnopqrstuvwxyz"

# 初始化Box实例，调用__init__方法
y = Box(x1)


print('----------------1---------------')
# 将Box实例当成“迭代器”用， 默认调用__iter__方法。 
#                             如果__iter__方法不存在，就调用__getitem__方法
for y1 in y:
    print(y1)


print('----------------2---------------')
# 调用__str__方法
print(y)


print('----------------3---------------')
# 调用__len__方法
print(len(y))


print('----------------4---------------')
# 调用append方法
y.append(1)
y.append("123456")


print('----------------5---------------')
# 调用__str__方法
print(y)


print('----------------6---------------')
# 调用__getitem__方法
print("y[3]=", y[3])


print('----------------7---------------')
# 判断item是否在表中, 调用.__contains__()方法
print( "10086" in y)


print('----------------8---------------')
# 调用__setitem__方法
y[0] = "fuck_begin"
print(y)
