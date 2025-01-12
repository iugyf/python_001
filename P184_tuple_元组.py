def enumerate(seq,start=0):
    rlist=[]
    for x in seq:
        # rlist.append((start,x))
        rlist.append((x,start))
        start+=1
    return rlist


seq = ['spring','summer','full','winter']
print(enumerate(seq))