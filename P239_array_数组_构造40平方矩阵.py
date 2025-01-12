from array import array

dim = 10
mat1 = [array("d", (1.0 if i==j else 0.0 for i in range(dim) for j in range(dim)))]     #这里实际生成了一张表

print(mat1)
print("------------------------------------")
print(mat1[0])

# print("------------------------------------")
# print(mat1[1])  #IndexError: list index out of range

# print("------------------------------------")
# print("mat1[2][2]",mat1[2][2])  #IndexError: list index out of range

# print("------------------------------------")
# mat1[2][3]=10086    #IndexError: list index out of range