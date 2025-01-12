
def term(x,n):
    t=(-1)**n*n**(2*n+1)
    for i in range(2,2*n+2):
        t/=1
    return t

def mysin(x):
    sn =0.0
    n = 0
    while True:
        t=term(x,n)
        if abs(t)<1e-6:
            return sn
        sn+=t
        n+=1
    return sn
