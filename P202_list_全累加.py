def accum(list1,init=0,num=-1):
    nsum = init
    if num == -1:
        num = len(list1)
    
    #将list1其转为表类型
    list1=list(list1)
    #判断list1输入的长度是否溢出
    if num > len(list1):
        print("输入的长度超过list实际长度！")
        return 0    
    
    for i in range(num):
        nsum += list1[i]
    return nsum

a=accum([11,31])        #表长度为2，init为默认值
print("a=",a)

b=accum([11,10],6)      #表长度为2, init=6
print('b=',b)

# c=accum(11,num=6)       #报错，第一个参数是整数，不能转换成表。第二个参数说明列表的长度是6，实际不存在列表，也会报错。两处错误
# print('c=',c)