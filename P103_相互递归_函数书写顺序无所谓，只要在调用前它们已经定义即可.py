#P103_相互递归_函数书写顺序无所谓，只要在调用前它们已经定义即可
x1=int(input("x1="))

def even(n):
    if n==0:
        return True
    else:
        return odd(n-1)
    
#even(4)       #这里调用的even函数中包含当前还未定义的odd函数，会报错    
def odd(n):
    if n==0:
        return False
    else:
        return even(n-1)
    
print(even(x1))