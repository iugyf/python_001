# 摘处：通义千问2025-1-9


# multiprocessing 是 Python 标准库中的一个模块，它提供了一个类似于 threading 模块的 API，允许程序利用多核处理器的能力来并行执行任务。
#     与线程不同，multiprocessing 使用的是系统级别的进程，这意味着每个进程都有自己的Python解释器实例和内存空间，从而避免了
#     全局解释器锁（GIL）带来的限制。这对于CPU密集型任务特别有用。


# 以下是 multiprocessing 模块的一些核心概念和功能：
# ========================================================================
# 1. 创建进程
    # 可以使用 Process 类创建一个新的进程。你需要定义一个目标函数作为新进程的入口点，并可以传递参数给这个函数。
print("\n-----------------------------------------\n")
from multiprocessing import Process

def worker(name):
    print(f'Worker {name}')

if __name__ == '__main__':
    p = Process(target=worker, args=('Mike',))
    p.start()  # 启动进程
    p.join()   # 等待进程完成




#----------------------------------------------------------------
# 2. 进程间通信 (IPC)
    # multiprocessing 提供了几种方式进行进程间的通信：


# 队列（Queue）：用于在进程之间安全地传递消息。
print("\n-----------------------------------------\n")
from multiprocessing import Process, Queue

def send(q):
    q.put("Hello from sender")

def receive(q):
    msg = q.get()
    print(msg)

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=send, args=(q,))
    p2 = Process(target=receive, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()



#----------------------------------------------------------------
# 管道（Pipe）：适用于两个进程之间的双向通信。
print("\n-----------------------------------------\n")
from multiprocessing import Process, Pipe

def send(conn):
    conn.send([42, None, 'hello'])
    conn.close()

def receive(conn):
    print(conn.recv())

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p1 = Process(target=send, args=(child_conn,))
    p2 = Process(target=receive, args=(parent_conn,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()



#----------------------------------------------------------------
# 3. 共享状态
    # 虽然通常建议尽量避免共享状态，但在某些情况下可能需要这样做。multiprocessing 提供了多种方式实现这一点，
    # 比如使用共享内存、Value 和 Array 对象等。
print("\n-----------------------------------------\n")
from multiprocessing import Process, Value, Array

def modify(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)  # 'd' 表示双精度浮点数
    arr = Array('i', range(10))  # 'i' 表示整数

    p = Process(target=modify, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])




#----------------------------------------------------------------
# 4. 进程池（Pool）
    # Pool 可以简化管理多个工作进程的过程，尤其适合于需要并行执行的任务集合。
print("\n-----------------------------------------\n")
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(processes=4) as pool:  # 创建包含4个进程的池
        result = pool.map(f, range(10))  # 并行计算f(0), f(1), ..., f(9)
        print(result)



# ========================================================================
# 通过这些工具，multiprocessing 模块使得编写能够充分利用多核处理器能力的Python应用程序变得更加简单。
# 无论是处理CPU密集型任务还是需要跨进程通信的应用场景，multiprocessing 都提供了强大而灵活的支持。