text=str(input("请输入字符串："))
s=str(input("请输入要查找的子串："))

n, end = 0, len(text)
while True:
    n = text.find(s,n,end)          #find的用法：  字符串.find(子串,开始位置，结束位置)     如果没找到，返回-1
    if n<0:
        break
    print(n)
    n+=1

print("n=",n)

