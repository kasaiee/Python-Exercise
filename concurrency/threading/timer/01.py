from time import sleep
from threading import Timer, current_thread, enumerate

can_start_new_thread = True

def cancel_threads():
    global can_start_new_thread
    can_start_new_thread = False
    for thread in enumerate():
        if thread.name != 'MainThread':
            thread.cancel()

def do_something():
    sleep(1)
    print(current_thread().name, 'is in progress')


Timer(1, cancel_threads).start()

while can_start_new_thread:
    Timer(0, do_something).start()
    sleep(0.1)
