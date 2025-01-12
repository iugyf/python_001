from math import  sin, cos


def enumerate(seq,start=0):
    rlist=[]
    for x in seq:
        rlist.append((start,x))
        start+=1
    return rlist

en1=tuple(range(10))
print(enumerate(en1,))

en2=tuple("abcdefg")
print(enumerate(en2,))

en3=('ab','cd','e','f',00,"01")
print(enumerate(en3,))



#----------------------------------------------------------------
#元组本身不能改变，但能包含能改变的元素
print("---------------")
print("元组本身不能改变，但能包含能改变的元素")

u=tuple("abc")
v=u,(1,2,3)
print("v=",v)

w=u,[1,2,3]     #含能改变的元素:表中的元素
print("w=",w)

w[1][1]=10086
print("w=",w)


#----------------------------------------------------------------
#元组在循环中应用
print("---------------")
print("元组在循环中应用")


square=lambda x: x*x
for i in square(2),sin(5.12), cos(6.77), 8.05,"fuck",int("10086"):
    print(i)