


def read_floats(frame):
    infile = open(frame)
    while True:
        line = infile.readline()
        if not line:
            infile.close()
            return
        yield from map(float, line.split())




def read_float_files(fname_list):
    for fname in fname_list:
        yield from read_floats(fname)



x = read_float_files("P311_浮点数据.txt")
print(type(x),x)

# print(x())    # 函数x是一个生成器对象，返回的是一个迭代器。它不是以return语句为返回值的一般函数