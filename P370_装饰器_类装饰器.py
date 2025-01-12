# 原书省略的代码来自：  P335_class_平面几何图形.py    与     P368_动态约束_虚函数.py
# 不过这些原代码都要改过来，让它们有继承关系。  
# 最终经过通义千问的修改，成了以下的样子：




# 类装饰器，用于为类添加计数功能
def add_counter(cls):
    # 使用单下划线来避免名称改写
    cls._objnum = 0
    
    # 保存原始的 __init__ 方法
    original_init = cls.__init__
    
    # 定义新的 __init__ 方法，增加计数
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        cls._objnum += 1
    
    # 替换原来的 __init__ 方法
    cls.__init__ = new_init
    
    # 定义一个类方法来获取计数值
    @classmethod
    def get_objnum(cls):
        return cls._objnum
    
    # 将类方法绑定到类上
    cls.get_objnum = get_objnum
    
    return cls


# Shape 类
@add_counter # 这里是用"Shape"这个类去装饰"add_counter"函数，所以这个类会把自己当作参数传到"add_counter"中，即：add_counter中的第一个参数"cls"
class Shape:
    def name(self):
        return "Shape"
    
    def show(self):
        print("I am a", self.name() + ".", "My area is", self.area())


# Point 类，继承自 Shape
class Point(Shape):
    def name(self):  # 重写 name 方法
        return "Point"
    
    def __init__(self, x, y):
        super().__init__()  # 调用父类的 __init__
        self._x = x
        self._y = y
    
    def getx(self):
        return self._x
    
    def gety(self):
        return self._y
    
    def area(self):  # 点没有面积
        return 0
    
    def move(self, delta_x, delta_y):
        self._x += delta_x
        self._y += delta_y
    
    def show(self):  # 重写 show 方法
        print("I am a", self.name() + ".", "My coordinates are", (self._x, self._y), "and my area is", self.area())


# Rectangle 类，继承自 Shape
class Rectangle(Shape):
    def __init__(self, point, length, width):
        # 不再调用 super().__init__()
        self._point = point  # 这里的 point 也是一个 Shape 的子类实例
        self._length = length
        self._width = width
    
    def getx(self):
        return self._point.getx()
    
    def gety(self):
        return self._point.gety()
    
    def area(self):
        return self._length * self._width
    
    def move(self, delta_x, delta_y):
        self._point.move(delta_x, delta_y)
    
    def name(self):  # 重写 name 方法
        return "Rectangle"
    
    def show(self):  # 重写 show 方法
        print("I am a", self.name() + ".", "My coordinates are", (self.getx(), self.gety()), "and my area is", self.area())


# Circle 类，继承自 Shape
from math import pi

class Circle(Shape):
    def __init__(self, point, radius):
        # 不再调用 super().__init__()
        self._center = point  # 这里的 point 也是一个 Shape 的子类实例
        self._radius = radius
    
    def getx(self):
        return self._center.getx()
    
    def gety(self):
        return self._center.gety()
    
    def area(self):
        return self._radius**2 * pi
    
    def move(self, delta_x, delta_y):
        self._center.move(delta_x, delta_y)
    
    def name(self):  # 重写 name 方法
        return "Circle"
    
    def show(self):  # 重写 show 方法
        print("I am a", self.name() + ".", "My coordinates are", (self.getx(), self.gety()), "and my area is", self.area())


# 测试代码
print("Point:")
point1 = Point(2, 3)
point2 = Point(5, 6)
print(point1.getx(), point1.gety())
print(point2.getx(), point2.gety())

print("Rectangle:")
rect1 = Rectangle(Point(0, 0), 2, 3)
rect2 = Rectangle(Point(7, 5), 5, 6)
print(rect1.getx(), rect1.gety())
print(rect2.getx(), rect2.gety())

print("Circle:")
circ1 = Circle(Point(0, 0), 3)
circ2 = Circle(Point(7, 5), 6)
print(circ1.getx(), circ1.gety(), circ1.area())
print(circ2.getx(), circ2.gety(), circ2.area())

# 显示计数功能
print("\nP370代码显示：")
point1.show()
print("Number of objects created:", Shape.get_objnum())  # 通过 Shape 类名访问计数值


