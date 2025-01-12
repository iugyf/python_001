#！！！读写文件的对象要是可迭代对象，常用list,也可用tuple，str等。  可迭代对象：list\set\tuple\array\str\dict


# write函数：将字符输出到文件
outf = open(r"P255_write_文件写入\outfile1.dat","w")        # r"...\..."  方法：原始字符串：用于文件地址的"\"符号输入。
                                                           # 这里之所以要写入字文件夹名"P255_write_文件写入",是因为python打开的是当前大文件夹的地址，
                                                           # 所以默认直接在大文件夹下写出文件，无论本程序文件夹所在是否已经是子文件地址。
outf.write("generated integers:\n")
for i in range(10):
    outf.write(", ".join([str(i**2 + j) for j in range(10)]) + '\n')
    # outf.write(str([str(i**2 + j) for j in range(10)]))
outf.close()



# writelines函数：将一组字符输出到文件
outf_2 = open(r"P255_write_文件写入\outfile_2.dat","w")  
lines=[str(i) + '\n' for i in range(0,1001)]
outf_2.writelines(lines)
outf_2.close()