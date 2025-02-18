# 即：通过拆分表（或元组）对象的方法，给函数提供多个实参,
#    参考书P221页页尾：用两个星号，它是通过拆分字典的方式给函数提供一组关键字(字典的关键字字段)实参。

def mysum(*args):       #定义函数时，带*号的形参说明可以有任意多个参数被传入
    s=0
    for i in args:
        s += i          
    return s


x1=(1,2,3,4,5,6,7,8,9)     
print("x1合计：",mysum(*x1))
#print("x1合计：",mysum(x1))        #报错，把这个x1给mysum当参数用，即：mysum(x1),结果mysum的参数会变成:((1,2,3,4,5,6,7,8,9),)   即：元组中的元组

x2 = mysum(1,2,3,4,5,6,7,8,9)
print("x2合计：",x2)

x3=1,2,3,4,5
print("x3合计：",mysum(*x3))  #要带星号