def accum(list1,init=0):
    nsum = init
    for x in list1:
        nsum +=x
    return nsum

a=accum([1,2,3])
b=accum([5,7,10],a)

print("a=",a,'\n','b=',b)