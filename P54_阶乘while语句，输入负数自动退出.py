print("this is a factorial calculator. -1 to stop")
n=int(input("factorial for:"))

while n>=0:
    prod=1
    for i in range(2,n+1):
        prod=prod*i 
        
    print("thefactorial of",n," is ",prod)
    n=int(input("factorial for:"))

print("Bye")