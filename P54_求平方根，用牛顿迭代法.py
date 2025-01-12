x=float(input("square root for:"))

guess = 1.0

while guess * guess != x:
    guess = (guess+x/guess)/2

print(guess)

#如果求2.0的平方根，程序卡住，因为浮点数结果不精确，无法结束循环。