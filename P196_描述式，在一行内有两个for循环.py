n=6
print(tuple(i**2+j for i in range(1,n) for j in range(1,i)))    #两个for之前左括号之后的参数是要执行内容，第一个for是外层循环，第二个for是内层循环。 



print("--------------------------------")
def func(n):
    list1 = [x*n for x in range(n)]
    list2 = [n**2 for n in range(10)]
    print("list1:",list1)
    print("list2:",list2)

func(n)