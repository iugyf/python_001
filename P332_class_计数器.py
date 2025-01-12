class Counter:
    def __init__(self,init=0):
        self._count = init
    
    def inc(self): self._count += 1
    def dec(self): self._count -= 1 
    def value(self): return self._count 
    def reset(self): self._count = 0
    
    def __str__(self): return self._count
    def print(self): 
        print("重写print函数: ", self._count)

c1 = Counter()
c2 = Counter(10)

c1.inc()
c2.dec()
c2.dec()

print(c1.value())
c2.print()