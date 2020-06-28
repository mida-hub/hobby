import time
import concurrent.futures

def process_function(name, age):
    print(f'Process {name}: starting {age}')
    time.sleep(2)
    print(f'Process {name}: finishing {age}')

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        # executor.submit(process_function, 1, '12')
        # executor.submit(process_function, 2, '12')
        # executor.submit(process_function, 3, '12')
        # executor.submit(process_function, 4, '12')
        executor.map(process_function, ['Taro', 'Jiro', 'Saburo'], [1, 2, 3])