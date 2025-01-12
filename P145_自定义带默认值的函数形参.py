#P145_自定义带默认值的函数形参
def ratio(pre,post=10.0):
    return pre/post


print(ratio(100))       #ratio函数，输入时省略了默认形参
print(ratio(100,1))
