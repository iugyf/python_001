# 为什么当前线程一直是： MainThread？


# from threading import Thread      # 光有 “Thread” 类不够，还要有 “threading” 类
import threading
from datetime import datetime
import time


run_time = 10
time_inerval = 0.5



def myfunc(s, num, interval):
    n = 0
    for i in range(num):
        time.sleep(interval)

# 创建两线程
threading.Thread(target=myfunc, args=("th1", run_time, time_inerval)).start()
threading.Thread(target=myfunc, args=("th2", run_time, time_inerval)).start()

for i in range(run_time):
    print()
    print('当前线程是：' , threading.current_thread().name, threading.current_thread())

    for th in threading.enumerate():                                                    # enumerate(): 返回当时处于活动状态的线程表
        print(str(i) + ' ' + th.name + ':', "alive" if th.is_alive() else "not alive", end='\t')  # is_alive()：检查线程是否活动 
        if th is not threading.current_thread():                                        # current_thread(): 返回当前线程对象
            print("非_当前线程")
        else:
            print("是_当前线程")
        time.sleep(time_inerval)
        
print('\n当前线程是：' , threading.current_thread().name, threading.current_thread())
print("main thread terminates. 最后显示，等待上面线程先完成")
  