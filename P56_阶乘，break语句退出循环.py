print("this is a factorial calculator. -1 to stop")

while True:
    n=int(input("factorial for:"))
    if n<0:
        break
    
    prod=1
    for i in range(2,n+1):
        prod=prod*i
    
    print("the factorial of ",n," is ",prod)

print("Bye")