#关键字实参能改变print函数的默认输出方式
def print_fibsl(n):
    f1=0
    f2=1
    print(0,1,sep=", ",end='')      #输出：逗号与空格分隔。 输完：不换行，不空格
    for k in range(1,n):
        f1, f2 = f2, f2+f1
        print(",",f2,end='')        #输出：默认。   输完：不换行，不空格
    print('\n')

print_fibsl(12)

print('\n')
print('\n')
print('\n')

#print默认输出
def print_default(n):
    f1=0
    f2=1
    print(0,1)     
    for k in range(1,n):
        f1, f2 = f2, f2+f1
        print(",",f2)        
    print('\n')

print_default(12)