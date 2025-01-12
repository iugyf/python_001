sum = 0
n=0

while True:
    x=int(input("next integer:"))
    if x%2==0:
        sum+=x
        n+=1
        if n==10:
            break
    
print(sum,n)