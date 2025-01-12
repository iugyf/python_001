from time import time
from random import random

def test1(n):
    t = time()
    rands=[]
    for i in range(n):
        rands=rands+[random()]
    print("test1:",str(time()-t)+'s')

def test2(n):
    t = time()
    rands=[]
    for i in range(n):
        rands.insert(0,random())
    print("test2:",str(time()-t)+'s')
    
def test3(n):
    t = time()
    rands=[]
    for i in range(n):
        rands.append(random())
    print("test3:",str(time()-t)+'s')

test1(100000)
test2(100000)
test3(100000)
