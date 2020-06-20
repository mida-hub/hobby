import logging
import threading
import time
import os

def thread_function(name):
    logging.info(f'Thread: staring pid = {os.getpid()}')
    time.sleep(2)
    logging.info(f'Thread {name}: finished')

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(
        format=format,
        level=logging.INFO,
        datefmt='%H:%M:%S'
    )

    logging.info('Main: before creating thread')
    x = threading.Thread(target=thread_function, args=('Taro',), daemon=True)
    logging.info(f'Main: before running Thread pid = {os.getpid()}')
    x.start()
    logging.info('Main: wait for the thread finish')
    x.join()
    logging.info('Main: all done')

