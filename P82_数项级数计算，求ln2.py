def ln_2(num):
    ln2 = 0.0
    sign = 1
    for n in range(1, num+1):
        ln2 += sign * 1 / n
        sign *= -1
    return ln2

for i in range (100,200,10):
    print("first", i, "term of series for ln 2:", ln_2(i))