import os
import time
import multiprocessing

list_a = []

def process_function(name):
    print(f'sub process {name}. process_id = {os.getpid()}')
    time.sleep(2)
    list_a.append(name)
    print('Sub list', id(list_a))
    print('sub process end')

if __name__ == '__main__':
#     print(multiprocessing.cpu_count())
    sub = multiprocessing.Process(target=process_function, args=('Test',))
    sub.start()
    print(f'Main Process. process_id = {os.getpid()}')
    # time.sleep(3)
    sub.join()
    print('Main Process End')
    print('Main list', id(list_a))