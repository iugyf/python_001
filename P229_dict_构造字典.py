
a=10
p1 = {0:1,1:-3,10000:2}     #p1本身就是个字典
print(p1)

#构造字典，  pl:用于字典的关键字      a：字典关键字 与 字典值 的比例
def poly_num_times(a,p1):
    res={}  #创建空字典
    for d in p1:
        res[d] = p1[d]*a    #res[d]:字典关键字，   pl[d]*a: 字典的值
    return res


dict_1 = poly_num_times(a,p1)
print(dict_1)
print(type(dict_1))