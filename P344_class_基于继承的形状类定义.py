class Shape:        # 定义抽象类，即不能产生实例的类。 这是所有该类型数据的父类
    def area(self):     # 定义方法，什么也不做，一旦调用就引发异常
        raise NotImplemented    
    
    def move(self, delta_x, delta_y):   # 定义方法，什么也不做，一旦调用就引发异常
        raise NotImplemented
    








#####################################################
# 以下自己添加的代码：
# 点类
class Point(Shape):     # Point类，它的父类是 Shape
    def __init__(self, x, y):
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


# 矩形类，引用点类对象
class Rectangle(Shape):
    def __init__(self, point, length, width):
        self._point = point
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


# 圆类
from math import pi
class Circle(Shape):
    def __init__(self, point, radius):
        self._center = point
        self._radius = radius
    
    def getx(self):
        return self._center.getx()
    
    def gety(self):
        return self._center.gety()
    
    def area(self):
        return self._radius**2 * pi
    
    def move(self, delta_x, delta_y):
        self._center.move(delta_x, delta_y)







# 打印
print("point:")     # 点
point1 = Point(2,3)
point2 = Point(5,6)
print(point1.getx(), point1.gety())

point1.move(3,7)
print(point1.getx(), point1.gety())
print(point2.getx(), point2.gety())

print("Rectangle:") # 矩形
rect1 = Rectangle(Point(0,0),2,3)
rect2 = Rectangle(Point(7,5),5,6)
print(rect1.getx(), rect1.gety())

rect1.move(3,7)
print(rect1.getx(), rect1.gety())
print(rect2.getx(), rect2.gety())


print("Circle: ")   # 圆
circ1 = Circle(Point(0,0), 3)
circ2 = Circle(Point(7,5), 6)

print(circ1.getx(), circ1.gety())
circ1.move(3, 7)
print("move: ", circ1.getx(), circ1.gety())

print(circ1.area())
print(circ2.area())










# 计算所有形状的总面积
def area(slist):
    s = 0
    for x in slist:
        if isinstance(x, Shape):    # 判断该对象是否为形状类型
            s += x.area()
    return s

s_area = [point1, point2, rect1, rect2, circ1, circ2]
print("总面积：",area(s_area))