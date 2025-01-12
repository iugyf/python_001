x1=int(input("x1="))

def harmony(num):
    s=0
    n=0
    while s<num:
        n+=1
        s+=1/n
    return n

for i in range(1,x1):
    print(i,harmony(i))