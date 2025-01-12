# 点类
class Point:
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
class Rectangle:
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
class Circle:
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
print("point:")
point1 = Point(2,3)
point2 = Point(5,6)
print(point1.getx(), point1.gety())

point1.move(3,7)
print(point1.getx(), point1.gety())
print(point2.getx(), point2.gety())

print("Rectangle:")
rect1 = Rectangle(Point(0,0),2,3)
rect2 = Rectangle(Point(7,5),5,6)
print(rect1.getx(), rect1.gety())

rect1.move(3,7)
print(rect1.getx(), rect1.gety())
print(rect2.getx(), rect2.gety())


print("Circle: ")
circ1 = Circle(Point(0,0), 3)
circ2 = Circle(Point(7,5), 6)

print(circ1.getx(), circ1.gety())
circ1.move(3, 7)
print("move: ", circ1.getx(), circ1.gety())

print(circ1.area())
print(circ2.area())


# 判断是否为任一形状
def is_shape(x):
    return (isinstance(x, Point) or
            isinstance(x, Rectangle) or
            isinstance(x, Circle))

# 总面积
def area(slist):
    s = 0
    for x in slist:
        if is_shape(x):
            s += x.area()
    return s

# 计算“元组”中形状的总面积
print("area: ", area((circ1, rect1, rect2, point1)))
# 计算“表”中形状的总面积
print("area: ", area([circ1, rect1, rect2, point1]))