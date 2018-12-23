

import threading
import time

def print_time():
    while True:
        print(time.time())

def print_log():
    while True:
        print('loged')

thread1 = threading.Thread(target=print_time, name='print time')
thread2 = threading.Thread(target=print_log, name='log')
thread1.start()
thread2.start()

thread1.join()
thread2.join()