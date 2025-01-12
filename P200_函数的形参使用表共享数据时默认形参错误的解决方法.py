#方法一：
def append5_1(a,b=None):     
    if b is None:
        b=[]                #每次默认形参为空时，创建新表
    for i in range(5):
        b.append(a)
    return b


print("第一次调用空表：",append5_1(1,[]))
print("第二次调用空表，缺省参数：",append5_1(1))
print("第三次调用空表：",append5_1(1,[]))
print("第四次调用空表，缺省参数：",append5_1(1))        



#------------------------------------------------
print("-----------------")
#方法二：
def append5_2(a,b=[]):     
    b = list(b)             #每次都将旧表创建一个拷贝，无论传进来的形参是否为缺省
    for i in range(5):
        b.append(a)
    return b




print("第一次调用空表，缺省参数：",append5_2(2))
print("第二次调用空表，缺省参数：",append5_2(2))
print("第三次调用空表：",append5_2(2,[]))
print("第四次调用空表：",append5_2(2,[]))