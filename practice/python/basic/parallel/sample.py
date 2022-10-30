from asyncio import futures
from concurrent.futures import ProcessPoolExecutor
from random import random
from time import sleep

def func(x):
    rand = random() * 2
    print(f'key = {x}, sleep {rand}')
    sleep(rand)

def do_parallel():
    futures = set()
    
    with ProcessPoolExecutor(max_workers=3) as executor:
        for key in [1, 2, 3, 4, 5]:
            futures.add(executor.submit(func, key))
    
    finished = set()
    
    while finished != futures:
        for f in futures - finished:
            if f.done():
                f.result()
                finished.add(f)
                
if __name__ == '__main__':
    do_parallel()
