#print输出带关键字参数，还是有条件改变性质的关键字参数
for i in range(1,100):
    print(i,end=', ' if i%10 !=9 else "\n")