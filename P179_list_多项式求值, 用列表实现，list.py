
p=[1,5,10]
x=6
print(p)
print(x)

#----------------------------------------------------------------
#方法一
def eval_poly1(p,x):
    val=0
    x2=1
    for i in range(0,len(p)):
        val += p[i]*x2
        x2 = x2*x
    return val

print("----------")
print(eval_poly1(p,x))


# ----------------------------------------------------------------
#方法二:虽然不是正确答案，但方法可学习
def eval_poly2(p,x):
    val=0.0
    for i in range(len(p)-1,-1,-1):
        pass
        val += val*x+p[i]
    return val

print("----------")
print(eval_poly2(p,x))



#-----------------------------------------------------------------
#方法三:虽然不是正确答案，但方法可学习
def eval_poly3(p,x):
    val=0.0
    for a in reversed(p):           #reversed：内置函数：反射迭代器
        val += val*x+a
    return val

print("----------")
print(eval_poly3(p,x))