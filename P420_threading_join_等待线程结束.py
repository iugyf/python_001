# 另外 join()方法：拼接字符串功能， 见书P213页
# 在threading中的join方法是等待线程结束功能，它还能timeout参数，设置超时。  如果timeout=None，就是默认死等。见书P422页。

from threading import Thread
from datetime import datetime

def myfunc(s, num):
    n = 0
    for i in range(num):
        n += i
    print("\t[{}]: {} \t".format(s, n), datetime.now(), end = "\t{" + s + "}\n")


# 线程1
th1 = Thread(target=lambda: myfunc("1", 1000000))
# 线程2
th2 = Thread(target=lambda: myfunc("2", 1000000))
# 启动线程
th1.start()
th2.start()

# .join()方法：主线程要等待它调用的线程结束后才能继续执行。  即：本线程调用了 “th1” 与 “th2” 线程，要等到它们都完成了才能执行下一句。
th1.join()
th2.join()
print("main thread terminates. 最后显示，等待上面线程先完成")



print('\n\n上面:使用线程等待方法join()')
print("--------------------------------------------------")
print('下面:在同一个文件中,使用字符串拼接方法.join()\n')

str_1 = ['Hello','the','whorld']
str_2 = '_fuck~~~~'.join(str_1)
print('拼接前：',str_1)
print('拼接后：',str_2)
print()