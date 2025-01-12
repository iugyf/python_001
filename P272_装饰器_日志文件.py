
def log_func(fname):
    def deco(fun):
        def wrapper(*args, **kwargs):
            logfile.write(fun.__name__+ " starts.\n")
            logfile.flush()
            x = fun(*args, **kwargs)
            logfile.write(fun.__name__+ " ends.\n")
            logfile.flush()
            return x
        return wrapper
    if fname[-4] != '.log':
        fname = fname + '.log'
    logfile = open(fname, 'w',encoding='utf_8')
    return deco


log1=log_func("P272_日志文件_logfile1")     #单纯的调用log_func函数，用于创建日志文件，并不牵扯装饰器功能
log2=log_func("P272_日志文件_logfile2")

@log1
def func1(a,b):
    x = func2(a,b,3)
    return x+b

@log1
def func2(a,b,c):
    return a + b * c

@log2
def func3(a,b,c,d):
    return a+b*c-d

@log2
def func4(a,b,c,d,e):
    x=func3(a,b,c,d)
    y=func3(b,c,d,e)
    return x*y

print(func1(1,4))
print(func2(2,3,4))

x1 = func3(2,3,5,1)
x2 = func3(2,3,4,2)

a = func4(2,3,4,2,10)
b = func4(2,3,2,5,4)

print(x1+x2,a-b)
