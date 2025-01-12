from threading import Thread

def myfunc(s, num, other=None):
    if other is not None:
        other.start()
    n = 0
    for i in range(num):
        n += i
    print(str(i) + ',' + s)

th1 = Thread(target=myfunc, args=('Th1.', 20000000, None), daemon=True)     # daemon=True：说明这是个守护进程。  当主进程结束时，守护也会自动结束
th2 = Thread(target=myfunc, args=('Th2.', 10000000, th1))
th2.start()         # 激活线程对象： th2运行中激活th1
th2.join()   # 主线程等待th2执行完成，之后再执行下面的代码
print('last statement of the main.')

# 备注，此程序只有在命令行模式下：th1才能执行完。 如果是在本vscode中执行，当主程序执行完后，th1也会自动关闭。