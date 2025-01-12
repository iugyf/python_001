
#计数: 
#参数1：要被计数的字符串
#参数2：储存计数结果的字典
def char_count(s,**dic):            #直接将在原书的dic改成**dic，在调用此函数时直接创建字典
    for c in s:
        if not c.isalpha():     #判断字符是否为字母，若不是字母则路过该字符
            continue
        c = c.lower()           #将该字母变成小写
        dic[c]=dic.get(c,0)+1   #将字符存入对应的字典位置，    dic.get(c,0)：这个‘0’表示默认值，如果字典中没找到‘c’，就返回0
    return dic                              #直接返回计数结果

x1 = str(input("请输入要计数的字符串："))
print("该字符串中各字符出现的次数：")
print(char_count(x1))