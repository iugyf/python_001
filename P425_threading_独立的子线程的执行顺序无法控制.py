# 独立的子线程的执行顺序无法控制

from threading import Thread

class Th1(Thread):
    _num = 0
    
    def __init__(self):
        Thread.__init__(self, name='sub-thread' + str(Th1._num))
        Th1._num += 1

    def run(self):
        for i in range(3):
            n = 0
            for k in range(100000): n += k
            print('{}->{}'.format(self.name, i), n)
        print('\n', self.name + ' terminates. ')

for n in range(4):
    th = Th1()
    th.start()

print('\nmain finishes.\n')
