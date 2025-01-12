#这道题的原理我没弄懂，因为连审题都没审明白。
def num_ccoins(n):
    amount = [0,1,2,5,10,50,100]

    def ccoins(k,n):
        if n==0:
            return 1
        if k==1 or n<0:
            return 0
        return ccoins(k,n-amount[k])+ccoins(k-1,n)
    
    return ccoins(6,n)

print(num_ccoins(100))