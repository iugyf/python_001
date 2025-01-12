# next() 是 Python 中的一个内置函数，用于从迭代器（包括生成器）中获取下一个元素。每次调用 next() 时，
#           它会返回迭代器的下一个值，并将迭代器的状态更新为指向下一个元素。
#           如果迭代器已经没有更多元素可返回，next() 会抛出 StopIteration 异常。



def fibs_infgen():
    f1,f2 = 0,1
    while True:
        yield f1    #生成器函数
        f1, f2 = f2, f1+f2


fibs = fibs_infgen()
for i in range(20):
    print(next(fibs))

f20_40 = tuple(next(fibs) for i in range(20))
f41 = next(fibs)
print(f20_40) 
print(f41) 