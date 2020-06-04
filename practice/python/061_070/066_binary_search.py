
def binary_search(arr, target):
    left = 0 # 探索の左端
    right = len(arr) - 1 # 探索の右端

    for i in range(len(arr)):
        search_idx = (left + right) // 2 # 中間値
        # print(f'left:{left}')
        # print(f'right:{right}')
        # print(f'search_idx:{search_idx}')
        if arr[search_idx] == target:
            return search_idx
        elif arr[search_idx] > target:
            right = search_idx - 1
        elif arr[search_idx] < target:
            left = search_idx + 1

        if left > right:
            return -1

# a = [1, 2, 3, 4, 5, 6]
# for i in range(1, 7):
#     print(i, binary_search(a, i))

import time
start = time.time()
a = [x for x in range(50000000)]
print(binary_search(a, 5309808))
elapsed_time = time.time() - start
print (f'elapsed_time:{elapsed_time:.01f}[sec]')