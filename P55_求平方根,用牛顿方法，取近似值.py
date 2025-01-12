x=float(input("square root for:"))

guess = 1.0

while abs(guess * guess -x) > 1e-8:
    guess = (guess+x/guess)/2

print(guess)