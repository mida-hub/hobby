a = [3, 5, 8, 10, 14, 17, 21, 39]

def binary_search(key):
    # print('-'*20)
    # print(key)
    left = 0
    right = len(a) - 1

    while right >= left:
        mid = left + (right - left) // 2
        # print(left)
        # print(mid)
        # print(right)

        if a[mid] == key:
            return mid
        elif a[mid] > key:
            right = mid - 1
        elif a[mid] < key:
            left  = mid + 1

    return -1




print(binary_search(10))
print(binary_search(3))
print(binary_search(39))

print(binary_search(-100))
print(binary_search(9))
print(binary_search(100))
