import time
from time import sleep
from multiprocessing import Process

def compress_file(timer_process):
    sleep(5)
    timer_process.terminate()

def show_timer():
    start_time = time.time()
    while True:
        print(f'Time elapsed: {time.time() - start_time:.2f} seconds')
        sleep(1)

p1 = Process(target=show_timer)
p2 = Process(target=compress_file, args=(p1, ))

p1.start()
p2.start()