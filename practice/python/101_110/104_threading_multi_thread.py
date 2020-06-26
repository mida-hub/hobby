from threading import Thread
import time
import logging
from concurrent.futures import ThreadPoolExecutor

def thread_function(name):
    logging.info(f'Thread {name}: start')
    time.sleep(2)
    logging.info(f'Thread {name}: finish')

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(
        format=format,
        level=logging.INFO,
        datefmt='%H:%M:%S'
    )

    # threads = []
    # for name in ('Taro', 'Jiro', 'Saburo'):
    #     logging.info(f'Main: create and start {name}')
    #     x = Thread(target=thread_function, args=(name,))
    #     threads.append(x)
    #     x.start()
    # for i, t in enumerate(threads):
    #     logging.info(f'Main: before join {i}')
    #     t.join()
    #     logging.info(f'Main: thread done {i}')

    with ThreadPoolExecutor(max_workers=3) as executor:
        # executor.map(thread_function, ['Taro', 'Jiro', 'Saburo'])
        executor.submit(thread_function, 'Taro')
        executor.submit(thread_function, 'Jiro')
        executor.submit(thread_function, 'Saburo')
        executor.submit(thread_function, 'Shiro')

    print('Main finish')
