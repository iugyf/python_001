print([1 if i ==j else 0 for i in range(10)] for j in range(10))


print(tuple(i**2 +j for i in range(1,5) for j in range(1,i)))
#上面代码中有两个for, 从左到右：第一个是外层循环，第二个是内层循环。第一个for之前是循环体。类似下面的嵌套过程
for i in range(1,5):        
     for j in range(1,i):
        print(i**2 +j)