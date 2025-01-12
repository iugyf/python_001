#相关知识：质因数分解的结果是唯一的（不考虑质因数的顺序），这是由算术基本定理保证的：任何大于 1 的整数都可以唯一地表示为若干个质数的乘积。

def prime_factors(n):
    def nextpf(n):
        d=2
        while d*d<=n:       #在质因数分解算法中，我们通常只需要检查那些小于或等于n的质数。这是因为如果𝑛有一个大于𝑛的质因数𝑝，那么𝑛 必然还有一个小于n的质因数q，使得𝑛=𝑝×𝑞。因此，我们只需要检查小于或等于n的质数即可。
            if n%d==0:
                return d
            d+=1
        return n
   
    flist=[]
    while n != 1:
        p = nextpf(n)
        flist.append(p)
        n //= p      #与上面d*d<=n类似原理，不断分解成更小的数求质数
        
    return flist


print(prime_factors(124))
print(prime_factors(112233445566778899))