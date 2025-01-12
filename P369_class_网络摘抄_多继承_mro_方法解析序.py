# 摘自：通义千问 2025-1-2
# 问：多继承的方法解析序， __mro__属性，  mro()方法


# 答：
    # 在 Python 中，多继承（multiple inheritance）允许一个类从多个父类中继承属性和方法。
    # 当一个类有多个父类时，Python 需要确定调用方法的顺序，即 方法解析顺序（Method Resolution Order, MRO）。
    # MRO 决定了当一个方法被调用时，Python 会按照怎样的顺序查找该方法。

# Python 使用 C3 线性化算法 来计算 MRO，确保继承层次结构中的所有类都被正确地考虑，并且避免了潜在的冲突。C3 线性化算法保证了以下几点：
    # 子类优先于父类：子类的方法总是优先于父类的方法。
    # 父类的顺序保持不变：如果一个类从多个父类继承，父类的顺序在 MRO 中保持不变。
    # 单调性：如果一个类 B 继承自 A，那么 B 的 MRO 中，A 必须出现在 B 之后。
    # 查看 MRO

# Python 提供了两种方式来查看类的 MRO：
    # __mro__ 属性：这是一个只读的元组，包含了类及其所有基类的线性化顺序。
    # mro() 方法：这是一个类方法，返回一个包含类及其所有基类的列表，表示 MRO。



#############################################################################################
# 示例

# 单继承
    # 对于单继承的情况，MRO 很简单，就是从子类开始，依次向上查找父类，直到 object 类（所有类的基类）。
print("\n-----------------------------1-----------------------------")
class A:
    def method(self):
        print("A.method()")

class B(A):
    pass

print(B.__mro__)  # 输出: (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
print(B.mro())    # 输出: [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

    # 在这个例子中，B 类的 MRO 是 [B, A, object]，表示当调用 method() 时，Python 会首先在 B 中查找，然后是 A，最后是 object。




# --------------------------------------------------------------------------------------
# 多继承
    # 多继承的情况下，MRO 的计算会更加复杂，因为需要考虑多个父类的顺序。C3 线性化算法确保了所有父类的顺序都得到正确的处理。
print("\n-----------------------------2-----------------------------")
class A:
    def method(self):
        print("A.method()")

class B:
    def method(self):
        print("B.method()")

class C(A, B):
    pass

print(C.__mro__)  # 输出: (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(C.mro())    # 输出: [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

    # 在这个例子中，C 类的 MRO 是 [C, A, B, object]，表示当调用 method() 时，Python 会首先在 C 中查找，然后是 A，接着是 B，最后是 object。




# --------------------------------------------------------------------------------------
# 更复杂的多继承
    # 当继承层次结构变得更加复杂时，MRO 的计算也会变得更加复杂。C3 线性化算法确保了所有父类的顺序都得到正确的处理，即使存在多个共同的基类。
print("\n-----------------------------3-----------------------------")
class A:
    def method(self):
        print("A.method()")

class B(A):
    pass

class C(A):
    def method(self):
        print("C.method()")

class D(B, C):
    pass

print(D.__mro__)  # 输出: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(D.mro())    # 输出: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

    # 在这个例子中，D 类的 MRO 是 [D, B, C, A, object]。注意，尽管 B 和 C 都继承自 A，但 C 的 method() 会被优先调用，
    # 因为 C 在 MRO 中排在 A 之前。




# --------------------------------------------------------------------------------------
# 调用父类方法
    # 在多继承的情况下，如果你想要显式调用某个父类的方法，可以使用 super() 函数。super() 会根据 MRO 来决定调用哪个父类的方法。
print("\n-----------------------------4-----------------------------")
class A:
    def method(self):
        print("A.method()")

class B(A):
    def method(self):
        print("B.method()")
        super().method()

class C(A):
    def method(self):
        print("C.method()")
        super().method()

class D(B, C):
    def method(self):
        print("D.method()")
        super().method()

d = D()
d.method()


# 输出：
    # D.method()
    # B.method()
    # C.method()
    # A.method()

    # 在这个例子中，D 类的 method() 方法调用了 super().method()，这会根据 MRO 调用 B 类的 method()，
    # 然后 B 类的 method() 又调用了 super().method()，最终调用了 C 类的 method()，最后调用了 A 类的 method()。





#############################################################################################
# 总结
    # __mro__ 属性：返回一个元组，表示类及其所有基类的 MRO。
    # mro() 方法：返回一个列表，表示类及其所有基类的 MRO。
    # C3 线性化算法：确保子类优先于父类，父类的顺序保持不变，并且避免了潜在的冲突。
    # super() 函数：可以根据 MRO 调用父类的方法，适用于多继承场景。
    # 通过理解和使用 MRO，你可以更好地控制多继承的行为，并避免潜在的继承冲突。