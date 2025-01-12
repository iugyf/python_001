# 摘自：通义千问 2024-12-30
# 问：函数、方法、属性的区别



# #####################################################################
# 在 Python 中，函数、方法 和 属性 是三个不同的概念，它们各自有不同的用途和行为。
# 理解它们之间的区别对于编写清晰、高效的代码非常重要。下面我们将详细解释这三者的定义、用法以及它们之间的主要区别。

# #####################################################################
# 1. 函数 (Function)
# 定义：
    # 函数是独立的代码块，用于执行特定的任务。它可以在任何地方被调用，并且可以接受参数、返回值。
    # 函数通常定义在模块或全局作用域中，不属于任何类或对象。


# 语法：
def function_name(parameters):
    # 函数体
    return result  # 可选


# 示例：
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 输出: 8


# 特点：
    # 独立性：函数是独立的实体，不依赖于任何类或对象。
    # 可重用性：函数可以被多次调用，传递不同的参数以执行相同的操作。
    # 返回值：函数可以返回一个值（通过 return 语句），也可以不返回任何值（即返回 None）。


# 常见类型：
    # 普通函数：如上面的例子，定义在模块或全局作用域中。
    # 匿名函数（lambda 表达式）：一种简化的函数定义方式，适用于简单的操作。

multiply = lambda x, y: x * y
print(multiply(3, 4))  # 输出: 12
print("----------------------1-----------------------")








#####################################################################
# 2. 方法 (Method)
# 定义：
    # 方法是与类或对象关联的函数。它是类的一部分，通常用于操作类的实例（对象）或类本身。
    # 方法必须通过类的实例或类本身来调用，不能像普通函数那样直接调用。


print("----------------------2-----------------------")
# 语法：
class ClassName:
    def method_name(self, parameters):
        # 方法体
        return result  # 可选



# 示例：
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

circle = Circle(5)
print(circle.area())  # 输出: 78.53975



# 特点：
    # 与类或对象关联：方法必须通过类的实例或类本身来调用。
    # self 参数：实例方法的第一个参数通常是 self，表示当前实例。通过 self，方法可以访问实例的属性和其他方法。



# 类方法和静态方法：除了实例方法，类还可以定义类方法（使用 @classmethod 装饰器）和静态方法（使用 @staticmethod 装饰器）。
    # 类方法：第一个参数是类本身（通常命名为 cls），而不是实例。
    # 静态方法：不接收 self 或 cls 参数，类似于普通函数，但属于类的命名空间。

# 示例：
class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @staticmethod
    def describe():
        return "A circle is a shape with all points at the same distance from its center."

# 使用类方法
circle = Circle.from_diameter(10)
print(circle.radius)  # 输出: 5.0

# 使用静态方法
print(Circle.describe())  # 输出: A circle is a shape with all points at the same distance from its center.





######################################################################
# 3. 属性 (Attribute)
# 定义：
    # 属性是类或对象的变量，用于存储数据。它可以是实例属性（属于对象）或类属性（属于类）。
    # 属性可以直接访问，不需要调用括号（()），而方法需要调用括号。


# 语法：
    # 实例属性：在 __init__ 方法中定义，或者通过实例动态添加。
    # 类属性：在类定义中直接定义，属于类本身，所有实例共享。

print("----------------------3-----------------------")
# 示例：
class Person:
    species = "Homo sapiens"  # 类属性

    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age    # 实例属性

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.name)  # 输出: Alice
print(person2.age)   # 输出: 25
print(Person.species)  # 输出: Homo sapiens


# 特点：
    # 实例属性：每个实例都有自己独立的属性副本，修改一个实例的属性不会影响其他实例。
    # 类属性：所有实例共享类属性，修改类属性会影响所有实例。
    # 访问方式：属性可以通过点符号直接访问，不需要调用括号（()），而方法需要调用括号。


# 属性的高级用法：
    # 属性访问控制：你可以使用 @property 装饰器将方法伪装成属性，从而实现对属性的读取、写入和删除的控制。
print("----------------------4-----------------------")
class Person:
    def __init__(self, name, age):
        self._name = name  # 私有属性
        self._age = age    # 私有属性

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer")
        self._age = value

person = Person("Alice", 30)
print(person.name)  # 输出: Alice
person.age = 31
print(person.age)   # 输出: 31

# 在这个例子中，name 和 age 看起来像是普通的属性，但实际上它们是由方法管理的。
# @property 装饰器允许你控制属性的读取和写入行为，甚至可以在设置属性时进行验证。




######################################################################
# 4. 总结
# 概念	定义	                                            定义位置	            调用方式	                                         特点
# 函数	独立的代码块，用于执行特定任务，不属于任何类或对象。	模块或全局作用域	     function_name()	                                 独立、可重用，可以接受参数并返回值。
# 方法	与类或对象关联的函数，用于操作类的实例或类本身。	    类定义内部	            instance.method_name() 或 Class.method_name()	    必须通过类或实例调用，通常有 self 或 cls 参数。
# 属性	类或对象的变量，用于存储数据。	                      类定义内部或实例中	   instance.attribute_name	                           直接访问，不需要调用括号；可以是实例属性或类属性。


# 关键区别：
    # 函数 是独立的代码块，不属于任何类或对象，可以直接调用。
    # 方法 是与类或对象关联的函数，必须通过类或实例调用，通常用于操作类的实例或类本身。
    # 属性 是类或对象的变量，用于存储数据，直接访问而不需调用括号。