
#计算表中元素之和
def sum1(numbs):
    s=0
    for i in range(len(numbs)):
        s+=numbs[i]
    return s


#计算表中元素之和，另一种方式
def sum2(numbs):
    s=0
    for x in numbs:
        s+=x
    return s


#检查表里是否存在某个元素
def is_in(x,list1):
    for y in list1:
        if y==x:
            return True
    return False


#检查表里元素出现的次数
def count(x,list1):
    n = 0
    for y in list1:
        if y==x:
            n+=1
    return n


list1=list(range(100))
print(list1)

print(sum1(list1))
print(sum2(list1))
print(is_in(10,list1))
print(count(1,list1))
