infile = None   #文件对象
nlist = []      #每次提取的数据，即：行数据
crt = 0         #子串个数




#打开文件
def open_floats(fname):
    global infile
    infile = open(fname)
    return infile


#下一个数据
def next_float():
    global nlist, crt
    if crt == len(nlist):
        line = infile.readline()
        if not line:
            infile.close()
            return None
        nlist =line.split()
        crt = 0
    x = nlist[crt]
    crt += 1
    return float(x)





firename = None #全局文件名
#打开文件，返回第一个数据
def read_floats(fname):
    global firename

    #读取下一个数据
    if firename == fname and firename is not None :
        return next_float()
    
    #如果调用时没有文件名参数，则返回提示
    if fname is None:
        return print("请输入要打开的文件名")
    
    #第一次调用本函数时:打开文件并返回第一个数据
    if firename is None and fname is not None:
        firename = fname
        open_floats(fname)
        return next_float()
    

def read_close():
    infile.close()