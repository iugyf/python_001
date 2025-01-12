b=[0,20,3]
s=0

# for i in range(b):     #系统报错，下一句代码说: TypeError: 'list' object cannot be interpreted as an integer  
#    s+=i                #类型错误：‘list’对象不能被解释为整数
# print(s) 

for i in range(*b):      #这里range(*b)就是range(0,20,3),即从0到20，单步进3。 即0+3+6+9+12+15+18=63
    s+=i
print(s)        #结果是63
