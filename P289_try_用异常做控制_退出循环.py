try:
    x = 0
    z=0
    while x<1000:
        y=0
        while y<100:
            if x+y>765:
                raise StopIteration(x,y,z)
            y+=37
            z+=1/(x-y-447)
        x+=17

except (StopIteration, ZeroDivisionError)as ex:     #可捕获两个异常，其中stopiteration是循环机制，严格来说不是异常，但此处捕获它就能使执行退出循环体。
    print(type(ex))
    if type(ex)==StopIteration:
        print("--------------------------------")
        print(ex.args[0],ex.args[1],ex.args[2])
   