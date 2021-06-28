n, k = map(int, input().split())
an = list(map(int, input().split()))

def is_ok(index, key):
    if an[index] >= key:
        return True
    else:
        return False

def binary_search(key):
    left = -1
    right = len(an)

    while (right - left > 1):
        mid = left + (right - left) // 2

        if is_ok(mid, key):
            right = mid
        else:
            left = mid

    return right

print(binary_search(k))
