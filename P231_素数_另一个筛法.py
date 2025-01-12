#检查当前的数(cand)是否为素数，若是则加入素数表(plist)中
def prims_n(n):
    def is_prime(cand,plist):  
        for p in plist:         #用素数表去筛选当前的数是否能被素数表整除，若能则不是素数
            if cand % p ==0:
                return False
            if p*p > cand:      #只要已经检查到素数表中的数的平方大于当前要检测的数，就说明梁明数不是素数
                return True
        
    plist = [2]     #素数列表
    num =1          #前n项的起始计数
    cand = 3        #当前检查是否为素数的数
    
    while num<n:
        if is_prime(cand, plist):   #调用检查是否为素数的函数
            plist.append(cand)      #将新的素数加入素数表中
            num += 1                #素数个数加1
        cand += 2                   #下一个要检查的数，加2是因为只需检查奇数，（偶数一定能被2整数，其实+3也行，因为3本身也是素数，如果被3整除那它就不是素数）

    return plist


x1 = int(input("请输入要求的前n项素数："))
print(prims_n(x1))