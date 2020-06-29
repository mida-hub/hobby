from multiprocessing import Process, Array, Value
import time

# def append_num(arr, num):
#     arr.append(num)

# def append_num(arr, idx, num):
#     arr[idx] = num

def append_num(arr, summary, idx, num):
    arr[idx] = num
    summary.value += num

if __name__ == '__main__':
    # arr = []
    # append_num(arr, 1)
    # append_num(arr, 2)

    arr = Array('i', [3, 3, 3])
    summary = Value('i', 10)
    p1 = Process(target=append_num, args=(arr, summary, 0, 1))
    p2 = Process(target=append_num, args=(arr, summary, 1, 2))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    time.sleep(2)

    print(arr[:])
    print(summary.value)