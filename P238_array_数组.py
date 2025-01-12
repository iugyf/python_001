#array数组类型使用方法：
#   1.要先导入array包，   即 import array 或 from array import array
#   2.数组所有元素都属于同一类型（与表不同）
#   3.数组类型创建后不可变
#   4.数组效率比表高

from array import array

int_array = array("i")
float_array = array("d",[i*0.1 for i in range(10)])

print(int_array,type(int_array))
print("-----------------1.-------------------")
print(float_array,type(float_array))
print("-----------------2.-------------------")
print(len(float_array))
print("-----------------3.-------------------")
for i in range(len(float_array)):
    print(float_array[i])

# print("----------------4.--------------------")
# int_array.append(2**100)    #OverflowError: Python int too large to convert to C long
# print(int_array)

print("-----------------5.-------------------")
int_array.extend([1,2,3,4,5,6,7,8,9,10])
print(int_array)