def sieve(n):

    #在表中筛选出素数，不是素数的元素置0值
    def sieve0(nlist):
        nlist[0]=nlist[1]=0
        k=2
        while k*k<=n:
            if nlist[k]!=0:
                for i in range(2*k,n+1,k):
                    nlist[i]=0
            k+=1
        return nlist

    #将已筛选出来的素数加入一张新表中
    def collect(nlist):
        primes=[]
        for x in nlist:
            if x!=0:
                primes.append(x)
        return primes

    #如果表元素个数少于2，返回空表        
    if n<2:
        return []

    #创造一个从小到大，n个元素的表，用于筛选素数
    numbs = sieve0(list(range(n+1)))

    return collect(numbs)

#打印出素数表
print(sieve(1000))

print("")

#打印出顺序表
print(list(range(100)))