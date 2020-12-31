import multiprocessing
import time

def process_function(name):
    print(f'Process {name}: start')
    time.sleep(2)
    print(f'Process {name}: end')

if __name__ == '__main__':
    print('Main Start')
    process_list = []
    for index in range(3):
        process = multiprocessing.Process(target=process_function, args=(index,))
        process_list.append(process)
        process.start() # 子プロセスの処理開始
    
    for index, process in enumerate(process_list):
        print(f'Main: before join {index}')
        process.join() # プロセスの処理が終わるのを待つ
        print(f'Main: after join {index}')
