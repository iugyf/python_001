
def fact(n):
    prod = 1
    for k in range(2,n+1):
        prod *=k
    return prod


while True:
    n=int(input("Next int:"))
    if n<0:
        break
    print("factorial of ", n ," is ", fact(n))

