import time
from time import sleep
from multiprocessing import Process

def do_something(sleep_time):
    print('starting process with sleep time', sleep_time)
    time.sleep(sleep_time)
    print('ending process with sleep time', sleep_time)

def terminate_all_after_2_seconds(process_list):
    start = time.time()
    while True:
        sleep(1)
        end = time.time() - start
        if end > 2:
            for process in process_list:
                process.terminate()
            break

process_list = [
    Process(target=do_something, args=(1,)),
    Process(target=do_something, args=(2,)),
    Process(target=do_something, args=(3,)),
    Process(target=do_something, args=(4,)),
]

for process in process_list:
    process.start()
    
Process(target=terminate_all_after_2_seconds, args=(process_list, )).start()