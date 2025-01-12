# threading使用中常见错误

import threading

def myfunc_1(s):
    n = 0
    for i in range(100):
        n += i
        print('\t' , s , '\t')

def myfunc_2(s):
    n = 0
    for i in range(100):
        n += i
        print('\t' + s +'\t')



# 创建两线程
# -------------------------------------------------------------------------
#    错误1：AttributeError: 'NoneType' object has no attribute 'join'
#     原因：在调用 start() 方法时使用了链式调用（即 threading.Thread(...).start()），这会导致 th1 和 th2 变量被赋值为 None，
#           因为 start() 方法返回的是 None，而不是线程对象本身。因此，当你尝试调用 th1.join() 时，
#           实际上是在 None 上调用 join()，从而引发了 AttributeError: 'NoneType' object has no attribute 'join' 错误。
# th1 = threading.Thread(target=myfunc_1, args=("th1")).start()
# th2 = threading.Thread(target=myfunc_2, args=("th2")).start()
# th1.join() 
# -------------------------------------------------------------------------
th1 = threading.Thread(target=myfunc_1, args=('th1',))      # 错误2：之所以 args=('th1',) 中有逗号，是因为错误提示：TypeError: programming finishedmyfunc_2() takes 1 positional argument but 3 were given  参数传太多？ 是这个解释器无法确认有多少个参数传入
th2 = threading.Thread(target=myfunc_2, args=('th2',))
th1.start()
th2.start()
th1.join()   

print("programming finished")


# 错误3：RuntimeError: can't create new thread at interpreter shutdown 错误通常发生在 Python 解释器正在关闭时尝试创建新线程的情况下。
    # 常见原因： 包括主线程退出过快、使用守护线程、信号处理不当等。
    # 解决方法： 包括确保主线程等待所有子线程完成、避免使用守护线程（除非必要）、捕获并处理信号、确保线程在解释器关闭前完成、
    #           避免在 __del__ 方法中创建新线程，以及使用 concurrent.futures 模块来更好地管理线程。