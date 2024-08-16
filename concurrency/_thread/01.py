import time
import _thread

def say_hi(name):
    time.sleep(1)
    print('hi', name)

names = ['mmreza', 'Fatima', 'Mahboobeh', 'Saeed']
for name in names:
    _thread.start_new_thread(say_hi, (name, ))

input('Press enter to exit!\n')