# from threading import Thread      # 光有 “Thread” 类不够，还要有 “threading” 类
import threading
from datetime import datetime

def myfunc(s, num):
    n = 0
    for i in range(num):
        n += i
    print("\t[{}]: {} \t".format(s, n), datetime.now(), end = "\t{" + s + "}\n")

# 创建两线程
threading.Thread(target=myfunc, args=("th1", 1000000)).start()
threading.Thread(target=myfunc, args=("th2", 1000000)).start()

for th in threading.enumerate():                                        # enumerate(): 返回当时处于活动状态的线程表
    print('\n' + th.name + ':', "alive " if th.is_alive() else "not alive\n")     # is_alive()：检查线程是否活动
    if th is not threading.current_thread():                            # current_thread(): 返回当前线程对象
        print("\n非当前线程：" + th.name + '\n')

        th.join()   # 本线程将等待 “th” 线程结束之后，再执行一步代码，   此处的下一个代码是for循环里的下一循环

print("main thread terminates. 最后显示，等待上面线程先完成")

# 这个程序无法正常结束！ 我猜：只要当前线程不结束，最后一行的代码也不会执行，而最后一行代码所在就是当前进程。即：自己卡自己，一直卡死。
# 备注，此程序只有在命令行模式下，才能正常结束。