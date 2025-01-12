
from array import array

# int_array1 = array([i for i in range(10)])       # 报错：TypeError: array() argument 1 must be a unicode character, not list
# print(int_array1)

int_array2 = array("d",[i for i in range(10)]) 
print(int_array2)
print("----------------------------")
for i in int_array2:
    print(i)