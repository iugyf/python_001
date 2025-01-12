x1=int(input("请输入梵塔一共有多少块盘子："))
x2 = 'A'
x3 = 'B'
x4 = 'C'

def moveone(sfrom,sto):
    print("move a disk from",sfrom,"to",sto)


def henoi(n,sfrom,sto,sby):
    if n==1:
        moveone(sfrom,sto)
        return
    henoi(n-1,sfrom,sby,sto)
    moveone(sfrom,sto)
    henoi(n-1,sby,sto,sfrom)

henoi(x1,x2,x3,x4)
