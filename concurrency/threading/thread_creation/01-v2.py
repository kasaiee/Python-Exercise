import time
from threading import Thread

class MyThread(Thread):
    def __init__(self, target, args):
        super().__init__()
        self.target = target
        self.args = args
    
    def run(self):
        self.target(*self.args)

def say_hi(name):
    time.sleep(1)
    print('hi', name)

t1 = MyThread(target=say_hi, args=('mmreza', ))
t2 = MyThread(target=say_hi, args=('Fatima', ))
t3 = MyThread(target=say_hi, args=('Mahboobeh', ))
t4 = MyThread(target=say_hi, args=('Saeed', ))

t1.start()
t2.start()
t3.start()
t4.start()