import time
from threading import Thread

def say_hi(name):
    time.sleep(1)
    print('hi', name)

t1 = Thread(target=say_hi, args=('mmreza', ))
t2 = Thread(target=say_hi, args=('Fatima', ))
t3 = Thread(target=say_hi, args=('Mahboobeh', ))
t4 = Thread(target=say_hi, args=('Saeed', ))

t1.start()
t2.start()
t3.start()
t4.start()