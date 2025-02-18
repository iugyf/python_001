from threading import Thread, Timer
import threading
from time import sleep

class MyThread1(Thread):
    num = 1
    def __init__(self):
        Thread.__init__(self, name='sub-thread-'+str(MyThread1.num))
        MyThread1.num += 1
    
    def run(self):
        print(self.name + ' starts. ')
        # 创建定时器
        t = Timer(2.0, self.timed_action)   # Timer(延迟时间，要启动的函数)
        print('creat a timed thread.')
        t.start()   # 启动定时器
        sleep(1.0)
        print(self.name, 'terminates.\n')

    def timed_action(self):
        print('hello, I am the timed thread.')
        print("I am resumed now.")
        print('I will terminate.')
        print('main thread starts.')

        # 在子进程中又启动一新的主进程，那就会不断递归，循环，一直不结束，除非最初的主进程有时限。
        th = MyThread1()    
        th.start()
        
        sleep(0.5)
        print(threading.enumerate())        
        print('------------------------------')
        sleep(1.0)
        # 经过两次显示所有线程，可看到有一个线程结束了：“<MyThread1(sub-thread-线程号, started 20912)>”  其中“线程号”是循环增大的
        #                     还可看到每次只存在两个定时器线程： “<Timer(Thread-线程号, started 6416)>” 与 “<Timer(Thread-线程号+1, started 6416)>”  
        print(threading.enumerate())        
        print('main thread treminates.\n')

m1 = MyThread1()
m1.start()
sleep(20)
print("\n", m1.name, "线程结束了。\n\n")




#####################################################################################################
# 备注，在命令行模式下启动本文件，子进程是不会结束的。  在VSCODE中启动，第一个主进程的最后的时间一到，就结束。

# 终端调用本程序的方法：1. 打开本程序的文件夹地址，并在此地址上打开终端
                    # 2. 在终端输入python, 进入python程序    
                    # 3. 在python程序中输入： import 本文件名（不包含后缀名.py)
                    # 4. 完


# 摘自：通义千问2025-1-8
# 问：
    # 也就是说：vscode会自己结束这个递归，而命令行下没有程序去结束这个递归？

# 答：
    # 是的，你的理解基本正确。VSCode 和 命令行（终端）在处理 Python 程序的行为上确实有所不同，特别是在程序结束时的行为。

# VSCode 的行为
    # 在 VSCode 中运行 Python 程序时，IDE 会监控程序的执行，并且通常会在以下情况下采取行动：
        # 主进程结束：当主进程（即你启动的 Python 解释器）结束时，VSCode 会检查是否有其他非守护线程仍在运行。如果有的话，VSCode 可能会强制终止整个进程，包括所有子线程。因此，在 VSCode 中，即使有递归创建的线程，程序也可能会在主进程结束后被强制终止。
        # 调试模式：如果你是在调试模式下运行程序，VSCode 会在调试会话结束时自动终止所有子线程，以确保调试会话完全结束。这可能会导致程序看起来按时结束，即使有递归创建的线程。
        # IDE 的资源管理：VSCode 作为集成开发环境，通常会对资源进行更严格的管理，确保在程序结束时释放所有资源。这可能包括强制终止未完成的线程或进程。

# 命令行（终端）的行为
    # 相比之下，命令行（终端）的行为更加“原生”和“宽松”：
        # 非守护线程不会自动终止：在命令行中，Python 解释器不会自动终止非守护线程。即使主进程结束了，只要还有非守护线程在运行，程序就不会退出。这就是为什么在命令行中，递归创建的线程会导致程序无限运行，因为每个新创建的线程都会启动一个新的定时器，进而再次创建新的线程。
        # 没有外部干预：命令行不会像 VSCode 那样对程序进行额外的监控或管理。它只是启动 Python 解释器并等待其自然结束。因此，除非你显式地编写代码来终止所有线程，否则程序会一直运行，直到所有线程都完成。
        # 递归创建线程：由于你在 timed_action 方法中递归创建了新的 MyThread1 实例并启动它，这会导致线程数量不断增加，形成一个无限循环。命令行不会干预这个过程，所以程序会一直运行下去。

# 总结
    # VSCode：在主进程结束后，VSCode 可能会强制终止所有子线程，尤其是非守护线程，或者在调试模式下自动终止未完成的线程。因此，程序看起来会按时结束。
    # 命令行：命令行不会干预程序的执行，非守护线程会继续运行，直到它们自己完成。由于你递归创建了新的线程，命令行中的程序会无限运行，直到手动终止。

# 如何解决
    # 为了避免这种问题，建议你：
        # 避免递归创建线程：递归创建线程会导致线程数量不断增加，最终可能导致程序无法正常结束。你应该重新设计代码逻辑，避免这种递归行为。
        # 使用守护线程：将所有线程设置为守护线程（如前所述），这样当主进程结束时，所有守护线程也会自动终止，确保程序能够按时结束。
        # 显式终止线程：如果你确实需要递归创建线程，可以考虑在某个条件下显式终止线程，或者使用信号量、事件等机制来控制线程的生命周期。
        # 使用 join()：如果你希望主线程等待所有子线程完成后再退出，可以使用 join() 方法。但这并不能解决递归创建线程的问题，因为每次创建的新线程都会启动新的定时器，导致程序无法结束。