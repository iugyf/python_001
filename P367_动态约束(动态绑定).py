
class B:
    def f(self):
        self.g()
    def g(self):
        print("B.g is called.")

class C(B):
    def g(self):
        print("C.g is called.")

x = B()
x.f()

y = C()
y.f()