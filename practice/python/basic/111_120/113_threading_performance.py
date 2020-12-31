import time
import concurrent.futures

max_size = 10000000
def run_function(num):
    for _ in range(max_size):
        num += 1
    return 1

# 通常の処理
def run_normal():
    start_time = time.time()
    for _ in range(4):
        run_function(1)
    end_time = time.time()
    print(f'normal: {end_time-start_time}')

# マルチスレッド
def run_by_multithread():
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(run_function, [1, 1, 1, 1])
    end_time = time.time()
    print(f'multi thread: {end_time-start_time}') 

# マルチプロセス
def run_by_multiprocess():
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        executor.map(run_function, [1, 1, 1, 1])
    end_time = time.time()
    print(f'multi process: {end_time-start_time}') 

if __name__ == '__main__':
    run_normal()
    run_by_multithread()
    run_by_multiprocess()
