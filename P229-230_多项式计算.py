#多项式计算，本程序自身就不完善，有很多限制，比如幂的进位、退位问题就没处理。 



#多项式：数乘，即：用一个数乘以一个多项式
def poly_num_times(a,pl):
    res = {}
    for d in pl:
        res[d]=pl[d]*a  #结果 = 项次的系数 * 乘数
    return res



#两多项式：相加
def poly_plus(p1,p2):
    res={}
    degrees = set(p1) | set(p2) #并集：两多项式各自的幂次的并集
    for d in degrees:
        coeff = p1.get(d,0) + p2.get(d,0)       #两多项式的相同幂次的系数相加
        if coeff != 0:
            res[d] = coeff
    return res



#两多项式：相乘
def poly_times(p1,p2):
    res={}
    for d1 in p1:
        for d2 in p2:
            d = d1+d2       #两幂相乘后的新幂
            coeff = res.get(d,0) + p1[d1]*p2[d2]        #res.get(d,0)是返回新幂的系数，如果不存在则返回0。  p1[d1]*p2[d2]：两幂的系数相乘
            if coeff ==0:
                if d in res:
                    del res[d]
            else:
                res[d]=coeff
    return res



#两多项式：判断是否相等
def poly_equal(p1,p2):

    if len(p1)!=len(p2):        #判断两多项式是否有相同的非0项
        return False
    
    for d in p1:                #每个同阶非0项比较是否相等
        if p1.get(d,0)!=p2.get(d,0):
            return False
        
    return True





#多项式。  用字典存储，关键字是幂次，即阶数； 值是系数
poly1={0:1,1:-3,10000:2}
poly2={1:3,2:-2,1000:5,10000:6}

p3=poly_plus(poly1,poly2)
p4=poly_num_times(3,p3)
p5=poly_times(poly1,poly2)

p6=poly_times(p3,p4)
p7=poly_times(p4,p3)


print("p1=",poly1)
print("p2=",poly2)
print("p3=",p3)
print("p4=",p4)
print("p5=",p5)
print("p6=",p6)
print("p7=",p7)

print("p6=p7?",poly_equal(p6,p7))
print("p6=p7*2?",poly_equal(p6,poly_num_times(2,p7)))