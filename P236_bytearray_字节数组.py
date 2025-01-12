b1 = b'this is a bytes'

ba1 = bytearray()
ba2 = bytearray(b1)
ba3 = bytearray(10)
ba4 = bytearray(range(45,60))

print("ba1:",ba1,"  ",type(ba1))
print("ba2:",ba2,"  ",type(ba2))
print("ba3:",ba3,"  ",type(ba3))
print("ba4:",ba4,"  ",type(ba4))


print("--------------------------------------------")
# ba1[0]=1    #IndexError: bytearray index out of range
# ba1[0]='a'  #TypeError: 'str' object cannot be interpreted as an integer
# ba1[11]=1   #IndexError: bytearray index out of range

ba2[0]=1
print("ba2:",ba2,"  ",type(ba2))
# ba2[3]=15700                #ValueError: byte must be in range(0, 256)
# print("ba2:",ba2,"  ",type(ba2))
# ba2[3]='abc'    #TypeError: 'str' object cannot be interpreted as an integer
# print("ba2:",ba2,"  ",type(ba2))