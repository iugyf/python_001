n=int(input("factorial for:"))

prod=1
for i in range(2,n+1):
    prod=prod*i

print("the factorial of ",n," is",prod)