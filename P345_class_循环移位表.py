class RotatableList(list):      # 继承list类
    
    # 循环左移，  num是移动次数，每次移一位
    def rot_left(self, num):    
        if not self or len(self) == 1:    # 空表或表中只一个元素时，直接返回
            return
        for i in range(num):
            x = self.pop(0)     # 弹出表头
            self.append(x)       # 加入表尾

    #循环右移
    def rot_right(self, num):   
        if not self or len(self) == 1:
            return
        for i in range(num):
            x = self.pop()
            self.insert(0, x)

# 准备测试数据
ls = RotatableList()
for i in range(10):
    ls.append(i)
print(ls)

# 左移3位
ls.rot_left(3)
print(ls)
# 右移7位
ls.rot_right(7)
print(ls)

ls1 = RotatableList((1,2,3,4,5,6))  # 为什么双括号, 明白了，如果单括号就是把这6个数当成6个参数传入，但list只接收一个参数，
                                    # 所以有第二个括号把括成一个参数(即元组类型)传入，（当元组类型传入后，list函数自动将其转换成表类型）。
print(ls1)
# x = list(7,8,9,10)     # list报错，参数个数多于1
x = list((7,8,9,10))     # 同样使用双括号，成功。
print(x)

ls2 = RotatableList("good lucky!")
print(ls2)
ls2.rot_right(5)
print(ls2)