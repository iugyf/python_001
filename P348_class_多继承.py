from P333_class_cls类方法_计算类被调用次数 import Countable
from P345_class_循环移位表 import RotatableList

print("----------------------------------------------------------")
print("-----------以上的头文件自带的输出，别管它-----------------")
print("----------------------------------------------------------\n")

class CRList(Countable, RotatableList):    # 多继承
    def __init__(self, *args, **kwargs):    # 第一个参数self是指向本实例对象的变量， 第二个参数是能输入任意多个参数的表， 第三个参数是能输入任意多参数的字典
        Countable.__init__(self)                        # 初始化父类
        RotatableList.__init__(self, *args, **kwargs)   # 初始化父类

ls1 = CRList([1,2,3,4,5,6,7,8,9,0])
ls2 = CRList("hello, countable and rotable list!")

ls2.rot_left(3) # 左移3位
print(ls2[:10]) # 打印ls2从头开始到第10个字符

ls1.rot_right(7) # 右移7位
print(ls1[:5])

print(CRList.get_count())   # 显示本类被调用次数，这比原书上的调用次数多，那是因为我在头文件 “P333_class_cls类方法_计算类被调用次数” 中已经调用过三次了。
                            # 也就是说，父类的类属性与子类共享。