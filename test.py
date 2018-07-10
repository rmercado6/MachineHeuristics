import time
from threading import Condition, Thread, Event, Semaphore

cond =Condition()
#
# for i in range(3):
#     cond.append(Condition())

def functionwait(i):
    time.sleep(1)
    cond.acquire()
    print(" - ")
    cond.wait()
    cond.release()

def functionnotify(i):
    time.sleep(1)
    cond.acquire()
    print(" - ")
    cond.notify()
    cond.release()


array = []
for i in range(3):
    array.append(Thread(target=functionwait, args=(i), name=i+1))
    array.append(Thread(target=functionnotify, args=(i), name=i+1))
    array[-1].start()
    array[-2].start()


for i in array:
    i.join()
