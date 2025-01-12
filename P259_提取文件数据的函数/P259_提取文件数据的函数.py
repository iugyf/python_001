import P259_头文件 as rf


fire_name = "P259_提取文件数据的函数\\数据.dat"
fs_1 = rf.open_floats(fire_name)
for i in range(10):
    print(rf.next_float())
print("\n")

fs_1.close()



#================================================================

next_number = lambda fire_name: rf.read_floats(fire_name)

print(next_number(fire_name))

for i in range(10):
    print(next_number(fire_name))
print("-------------------------")

#fs_1.close()
rf.read_close()