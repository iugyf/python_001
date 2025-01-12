begin_1=int(input("开始位置:"))    
end_1=int(input("结束位置:"))  
high_1=int(input("高度:"))
ch_1=str(input("用于填充的字符:"))    



#实心线
def line(begin,end,ch):
    s=''
    for i in range(0,begin):
        s+=" "
    for i in range(begin,end+1):
        s+=ch
    return s


#空心两端点
def ends(first,second, ch):
    
    s=''
    
    for i in range(0,first):
        s+=" "
    
    s+=ch
    
    if first < second:
    
        for i in range(first+1,second):
            s+=' '
        
        s+=ch
    
    return s



#空心矩形
def rect(begin,len,high,ch):
    print(line(begin,len,ch))

    for i in range(high-2):
        print(ends(begin,len,ch))

    print(line(begin,len,ch))



#实心矩形
def rect_fill(begin,len,high,ch):
    for i in range(high):
        print(line(begin,len,ch))



#画线
#print(line(begin_1,end_1,ch_1))
#print(ends(begin_1,end_1,ch_1))



#画矩形
rect(begin_1,end_1,high_1,ch_1)
print('\n')
rect_fill(begin_1,end_1,high_1,ch_1)