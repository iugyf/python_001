def rev(list1):
    #判断是否为“表”类型
    if not isinstance(list1,list):
        return 
    #反转表内各元素
    for i in range(len(list1)//2):
        #list1[i] = list1[-i-1]         #这样只转前半部分的元素
        list1[i], list1[-i-1] = list1[-i-1], list1[i]
    
a1=[1,2,3,4,5,6,7]
a2=[1,2,3,4,5,6,7,8,9,10]

print("original a1:",a1)
rev(a1)
print("after rev:",a1)

print("-------------------")

print("original a2:",a2)
rev(a2)
print("after rev:",a2)