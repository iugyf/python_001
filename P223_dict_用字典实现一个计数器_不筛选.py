
#计数: 
#参数1：要被计数的字符串
#参数2：储存计数结果的字典
def char_count(s,**dic):
    for c in s:

        #不用筛选了，直接全上吧
        # if not c.isalpha():     #判断字符是否为字母，若不是字母则路过该字符
        #     continue
        # c = c.lower()           #将该字母变成小写
        
        dic[c]=dic.get(c,0)+1   #将字符存入对应的字典位置，    dic.get(c,0)：这个‘0’表示默认值，如果字典中没找到‘c’，就返回0
                                #dic[c]:  这个c是关键字，即把等号后面的值存入这个关键字下的值中
    return dic




str_1 = str(input("请输入要计数的字符串："))
print("该字符串中各字符出现的次数：")
dict_1 = char_count(str_1)      
print(dict_1)


#单个字符查询出现次数
str_2 = str(input("输入想查询出现次数的单个字符："))
print(dict_1.get(str_2,0))

if str_2 in dict_1:         #用下标查询字典里的关键字，若不存在会报错，所以这里用了if判断
    print(dict_1[str_2])
else:
    print(0)