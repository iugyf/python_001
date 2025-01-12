def primes():
    def is_primes(cn):
        for p in plist:
            if cn % p == 0:
                return False
            if p*p > cn:
                return True
            
    plist = [2]
    yield 2
    cn = 3
    while True:
        if is_primes(cn):
            plist.append(cn)
            yield cn
        cn += 2


if __name__ == '__main__':
    ps = primes()

    for i in range(10000):
        next(ps)
    
    print(next(ps))
    print(next(ps))
