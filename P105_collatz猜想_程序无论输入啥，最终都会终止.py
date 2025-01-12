
x1=int(input("x1:"))

def collatz(n):
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=n*3+1
        return 1
    
print(collatz(x1),"programming finished.")