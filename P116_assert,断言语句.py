


x1=input("x1:")     #默认输入类型：str

def fact(n):
    print("x1 type:",type(x1))

    assert isinstance(n,int) and n>=0  #assert:断言语句,如果条件不成立，程序就会报错 
                                       #isinstance:类型检查

    prod=1
    for k in range(2,n+1):
        prod =prod*k
    return prod

print("x1=",fact(x1))