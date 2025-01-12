class C:pass        #此类中原来啥也没有

x = C()
x.a = 1     #给已有类对象赋新属性
x.b = 2

print(x.a, x.b)
    
