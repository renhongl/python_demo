

from multiprocessing import Process
import os


def child_process(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=child_process, args=('test',))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end.')