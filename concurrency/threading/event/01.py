from time import sleep
from threading import Event, Thread

def download_file(event):
    print('starting download')
    sleep(3)
    print('download completed')
    event.set()

def compress_file(event):
    event.wait()
    print('starting compression')
    sleep(2)
    print('compression completed')

if __name__ == '__main__':
    event = Event()
    Thread(target=download_file, args=(event, )).start()
    Thread(target=compress_file, args=(event, )).start()