def read_floats(fname):
    nlist = []
    infile = open(fname,encoding = 'utf_8')
    crt = 0

    def next_float():
        nonlocal nlist, crt
        if crt == len(nlist):
            line = infile.readline()
            if not line:
                infile.close()
                return None
            nlist = line.split()
            crt = 0
        crt += 1
        return float(nlist[crt-1])
    
    return next_float           # 这个返回值不要加括号，此时返回的是内部函数，可以用于赋值给另一个函数。若加括号，则返回的是个浮点数


fname = "P266_数据文件.txt"
next_number = read_floats(fname)    # 此时next_number被赋值成函数

for i in range(10):
    print(next_number())        
print("---------------------------------")