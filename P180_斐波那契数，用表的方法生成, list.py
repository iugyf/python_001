#----------------------------------------------------------------
#方法一：
def gen_fibs(n):
    fibs=[0]*(n+1)
    fibs[1]=1
    for i in range(2,n+1):
        fibs[i]=fibs[i-1]+fibs[i-2]
    return fibs

fs = gen_fibs(20)
print("First",str(len(fs)),"Fibonacci numbers:",fs)


#----------------------------------------------------------------
#方法二：
def gen_fibs2(n):
    fibs=[0,1]
    for i in range(2,n+1):
        fibs.append(fibs[-2]+fibs[-1])
    return fibs

fs = gen_fibs(20)
print("First",str(len(fs)),"Fibonacci numbers:",fs)