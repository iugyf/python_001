x1 = int(input("请输入两个要求公约数擞，用回车键分隔"))
x2 = int(input())


def gcd(m,n):
    if n%m==0:
        return m
    return gcd(n%m,m)

print(gcd(x1,x2))
