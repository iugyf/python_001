x=float(input("\n square root for:"))

def sqrt(x):
    guess = 1.0
    n=0

    while abs(guess * guess -x) > 1e-8:
        guess = (guess+x/guess)/2
        n=n+1
        print(n,guess)

    return("\n",guess,"\n")     #这个返回值显示的是：('\n', 3.162277660168379, '\n')

print(sqrt(x))