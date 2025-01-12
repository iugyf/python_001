def fibs_closure(limit):
    f1, f2 = 0,1
    i = 0

    def generator():
        nonlocal i, f1, f2
        if i == limit:
            return None
        tmp = f1
        f1, f2 = f2, f1 + f2
        i += 1
        return tmp
    
    return generator

fibs = fibs_closure(30)
for i in range(20):
    print(str(i)+": ",fibs())

while True:
    x = fibs()
    if x is None:
        break
    print(x)