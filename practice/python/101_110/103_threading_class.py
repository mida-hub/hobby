from threading import Thread
import time
import logging

class MyThread(Thread):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def run(self):
        logging.info(f'Thread {self.msg} start')
        time.sleep(2)
        logging.info(f'Thread {self.msg} end')

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(
        format=format,
        level=logging.INFO,
        datefmt='%H:%M:%S'
    )

    x = MyThread('Hello Sub Thread')
    x.start()
    logging.info('Main Start')
    x.join()
    logging.info('Main End')
    