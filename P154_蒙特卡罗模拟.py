#此程序有概率出现除0错误，这是原程序自身编程问题

from random import randrange

#蒙特卡罗模拟：框架函数
def montecarlo(test,num):
    passed=0
    for i in range(num):
        if test():
            passed +=1
        return passed/num
   

#求出最大公约数
#suppose m>=0, n>0
def gcd(m,n):
    if m%n == 0:
        return n
    return gcd(n,m%n)

#测试最大公约数是否为1，返回布尔值
def pi_test():
    a = randrange(1,2**31)
    b = randrange(1,2**31)
    return gcd(a,b)==1


#主函数，也就是入口
def my_test(num):
    return (6 / montecarlo(pi_test,num))**0.5


print("my_test:",my_test(100))
print("my_test:",my_test(1000))
#print("my_test:",my_test(10000))
# print("my_test:",my_test(100000))