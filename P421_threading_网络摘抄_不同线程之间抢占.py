import threading
import time

run_time = 20
time_inerval = 1


def myfunc(s, num):
    n = 0
    for i in range(num):
        time.sleep(time_inerval)
        print('\n' + str(i) + "\t当前线程是：" + str(threading.current_thread()))    #  threading.current_thread() 当前线程

# 创建两线程
threading.Thread(target=myfunc, args=("th1", run_time,)).start()
threading.Thread(target=myfunc, args=("th2", run_time,)).start()

for i in range(run_time):
    print('\n' + '当前线程是主线程：' + str(i) + '\t' + str(threading.current_thread())) 
    time.sleep(time_inerval)

print("main thread terminates. 最后显示，等待上面线程先完成")
