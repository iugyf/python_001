def fib(n):
    fibs={0:0, 1:1}     #斐波那契数前两项

    def fib0(k):
        if k in fibs:
            return fibs[k]
        fibs[k] = fib0(k-2) + fib0(k-1)
        return fibs[k]
    
    return fib0(n)


x1 = int(input("请输入你要求的斐波那契数项："))
print(fib(x1))