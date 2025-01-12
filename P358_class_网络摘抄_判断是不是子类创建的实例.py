# 摘自：通义千问 2024-12-31
# 问：在父类中如何判断是不是子类创建的实例

# 答：
    # 在 Python 中，父类可以通过多种方式来判断当前实例是否是由子类创建的。这通常用于实现一些特定的行为，
    # 例如在父类中根据实例的类型执行不同的逻辑。以下是几种常见的方法来判断当前实例是否是子类的实例。


#####################################################################################################
# 1. 使用 isinstance() 检查实例类型
    # isinstance() 是 Python 内置的函数，可以用来检查一个对象是否是指定类或其子类的实例。
    # 通过使用 isinstance()父类可以判断当前实例是否是由子类创建的。

# 示例：
print("\n\n-----------------------------1------------------------------------")
class Parent:
    def __init__(self):
        if not isinstance(self, Parent):
            print("This instance is created by a subclass.")
        else:
            print("This instance is created by the Parent class.")

class Child(Parent):
    pass

# 创建 Parent 类的实例
p = Parent()        # 输出: This instance is created by the Parent class.

# 创建 Child 类的实例
c = Child()     # 输出: This instance is created by a subclass.



# 解释：
    # isinstance(self, Parent)：这个表达式会返回 True 如果 self 是 Parent 类或其子类的实例。
    # 在 Parent.__init__ 中，我们检查 self 是否是 Parent 类的实例。如果是，则说明实例是由 Parent 类直接创建的；否则，说明实例是由子类创建的。




#####################################################################################################
# 2. 使用 type() 和 __class__ 检查实例的具体类型
    # 如果你想更严格地检查实例的具体类型（即是否是子类的实例），可以使用 type() 或 self.__class__ 来获取实例的实际类型，并与父类进行比较。

# 示例：
print("\n\n-----------------------------2------------------------------------")
class Parent:
    def __init__(self):
        if type(self) is not Parent:
            print("This instance is created by a subclass.")
        else:
            print("This instance is created by the Parent class.")

class Child(Parent):
    pass

# 创建 Parent 类的实例
p = Parent()        # 输出: This instance is created by the Parent class.

# 创建 Child 类的实例
c = Child()     # 输出: This instance is created by a subclass.


# 解释：
    # type(self) is not Parent：这个表达式会返回 True 如果 self 的类型 “严格等于” Parent 类。如果 self 是子类的实例，
    # type(self) 将返回子类的类型，因此条件为 True。
    # type() 比较的是具体的类型，而不是继承关系。因此，只有当实例是由 Parent 类直接创建时，type(self) 才会等于 Parent。







#####################################################################################################
# 3. 使用 __class__.__name__ 获取类名
    # 你还可以通过 self.__class__.__name__ 获取当前实例所属类的名称，并根据类名来进行判断。

# 示例：
# Python
# 深色版本
print("\n\n-----------------------------3------------------------------------")
class Parent:
    def __init__(self):
        if self.__class__.__name__ != "Parent":
            print(f"This instance is created by the subclass: {self.__class__.__name__}")
        else:
            print("This instance is created by the Parent class.")

class Child(Parent):
    pass

# 创建 Parent 类的实例
p = Parent()        # 输出: This instance is created by the Parent class.

# 创建 Child 类的实例
c = Child()     # 输出: This instance is created by the subclass: Child


# 解释：
    # self.__class__.__name__：这个属性返回当前实例所属类的名称（作为字符串）。你可以根据类名来判断实例是由哪个类创建的。
    # 这种方法适用于你想要根据类名进行更灵活的判断，或者在日志记录中输出类名。




#####################################################################################################
# 4. 使用 __bases__ 检查类的基类
    # 如果你想要检查当前实例的类是否有父类（即是否是子类），可以使用 self.__class__.__bases__。__bases__ 是一个元组，包含当前类的所有基类。

# 示例：
print("\n\n-----------------------------4------------------------------------")
class Parent:
    def __init__(self):
        if Parent in self.__class__.__bases__:
            print(f"This instance is created by a subclass: {self.__class__.__name__}")
        else:
            print("This instance is created by the Parent class.")

class Child(Parent):
    pass

# 创建 Parent 类的实例
p = Parent()        # 输出: This instance is created by the Parent class.

# 创建 Child 类的实例
c = Child()     # 输出: This instance is created by a subclass: Child


# 解释：
    # self.__class__.__bases__：这个属性返回一个元组，包含当前类的所有基类。如果 Parent 在这个元组中，说明当前类是 Parent 的子类。
    # 这种方法适用于你想要检查当前类是否继承了某个特定的父类。




#####################################################################################################
# 5. 使用 super() 调用父类方法并传递信息
    # 有时你可能希望在父类中执行某些操作时，让子类能够传递额外的信息。你可以通过 super() 调用父类的方法，并在子类中重写该方法来传递信息。

# 示例：
print("\n\n-----------------------------5------------------------------------")
class Parent:
    def __init__(self):
        if hasattr(self, 'is_subclass'):
            print("This instance is created by a subclass.")
        else:
            print("This instance is created by the Parent class.")

class Child(Parent):
    def __init__(self):
        self.is_subclass = True
        super().__init__()

# 创建 Parent 类的实例
p = Parent()    # 输出: This instance is created by the Parent class.

# 创建 Child 类的实例
c = Child()     # 输出: This instance is created by a subclass.


# 解释：
    # 在 Child 类中，我们定义了一个属性 is_subclass，并在调用 super().__init__() 之前设置它。
    # 在 Parent 类中，我们使用 hasattr(self, 'is_subclass') 来检查是否存在 is_subclass 属性。如果存在，说明实例是由子类创建的。




#####################################################################################################
# 总结
    # isinstance(self, Parent)：最常用的方法，可以检查实例是否是 Parent 类或其子类的实例。推荐使用。
    # type(self) is not Parent：更严格的检查，只允许 Parent 类的实例通过，不允许子类的实例。
    # self.__class__.__name__：通过类名进行判断，适用于需要根据类名进行不同处理的情况。
    # self.__class__.__bases__：检查类的基类，适用于需要确认类继承关系的场景。
    # super() 和自定义属性：通过子类传递信息给父类，适用于需要在父类中根据子类行为做出不同响应的情况。
    # 选择哪种方法取决于你的具体需求。如果你只是想简单地判断实例是否是子类的实例，isinstance() 是最简洁和推荐的方式。
    # 如果你需要更复杂的逻辑或更严格的类型检查，可以选择其他方法。



# 以上代码有冲突，剪切到其它py文件中就行。