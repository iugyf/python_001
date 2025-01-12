
#计数: 
#参数1：要被计数的字符串
#参数2：储存计数结果的字典
def char_count(s,**dic):
    for c in s:

        #不用筛选了，直接全上吧
        # if not c.isalpha():     #判断字符是否为字母，若不是字母则路过该字符
        #     continue
        # c = c.lower()           #将该字母变成小写
        
        dic[ord(c)]=dic.get(ord(c),0)+1   #将字符存入对应的字典位置，    dic.get(c,0)：这个‘0’表示默认值，如果字典中没找到‘c’，就返回0
    return dic

x1 = str(input("请输入要计数的字符串："))
print("该字符串中各字符出现的次数：")
print(char_count(x1))