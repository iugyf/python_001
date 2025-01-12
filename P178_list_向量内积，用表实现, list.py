def vector_prod(v1,v2):
    #istance函数：判断第一个参数是否是第二个参数类型
    if not(isinstance(v1,list)) and isinstance(v2,list) and len(v1)==len(v2):
        return float("nan")
    prod = 0.0
    for i in range(len(v1)):
        prod += v1[i]*v2[i]
    return prod

p = vector_prod([1.2,5.3,4.23,7.44],[7.28,9.6,2.11,6.53])
print(p)
print(float("nan"))