def mean_variance_file(fname):
    num = 0
    fsum = 0.0
    data = []
    infile = open(fname)

    for line in infile:         #文件中的每行
        for s in line.split():  #每行中每个子串
            x = float(s)
            data.append(x)
            fsum += x
            num += 1
    
    if num == 0:
        return(0,0,0)
    mean = fsum / num

    fsum = 0
    for x in data:
        fsum += (x-mean)**2
    
    return(num,mean,(fsum/num)**0.5)        #返回值：个数，平均值，方差


fs_1 = "P257_文件操作_数据.dat"
print(mean_variance_file(fs_1))