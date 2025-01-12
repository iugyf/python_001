#自定义拷贝函数
def mat_copy(mat):
    return [[x for x in vec] for vec in mat]

a1=[[i+j for i in range(3)] for j in range(3)]
a2=mat_copy(a1)


#判断各个元素是否为同一个对象
def just_same(a1,a2,x,y):
    for i in range(x):
        for j in range(y):
            print("a1[",i,"][",j,"].id:",id(a1[i][j]))
            print("a2[",i,"][",j,"].id:",id(a2[i][j]))
            if a1[i][j] is a2[i][j]:
                print("the same")
            else:
                print("fuck~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~对象不同了")



print("对原a1元素有变动前：")
just_same(a1,a2,3,3)



print("===================================================")
print("===================================================")
print("===================================================")
print("现在改变a1的元素了：")
a1[1][2] = 10086
a1[0] = [666,666,666]
just_same(a1,a2,3,3)

print("这应该是“写时复制”功能。")