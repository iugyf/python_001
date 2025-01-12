# 类方法cls: 是所有类的实例的共同方法，与这个类的整体有关
# 类中实例对象self: 这是该类下某个实例的专有数据，专有方法


# 计算类被调用次数
class Countable:
    counter = 0

    def __init__(self):
        Countable.counter += 1      # 类对象Countable
    
    @classmethod    # 类方法
    def get_count(cls):
        return Countable.counter
    


print(Countable.get_count())
x = Countable()
print(Countable.get_count())
y = Countable()
print(Countable.get_count())
z = Countable()
print(Countable.get_count())

# 备注：该程序被 “P348_class_多继承.py" 文件中的类继承，当那子类调用父类方法（此处为Countable.__init__方法）时，counter的数值一样增大。