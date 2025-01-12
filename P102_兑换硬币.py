#这道题的题目我都没看懂，更不用说理解它的逻辑了。

x1 = int(input("x1:"))
x2 = int(input("x2:"))

def amount(k):
    if k==1:
        return 1
    if k==2:
        return 2
    if k==3:
        return 5
    if k==4:
        return 10
    if k==5:
        return 50
    if k==6:
        return 100
    
#参数1：币种
#参数2：人民币款额
def ccoins(k,n):
    if n==0:
        return 1
    if k==0 or n<0:
        return 0
    return ccoins(k,n-amount(k) + ccoins(k-1,n))

print(ccoins(x1,x2))