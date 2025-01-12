x=float(input("\n square root for:"))

guess = 1.0
n=0

while abs(guess * guess -x) > 1e-8:
    guess = (guess+x/guess)/2
    n=n+1
    print(n,guess)

print("\n",guess,"\n")