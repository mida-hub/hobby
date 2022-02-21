# 二分探索

import bisect

A = [1, 2, 3, 4, 5]
x = 1

print(bisect.bisect(A, x))
print(bisect.bisect_left(A, x))
print(bisect.bisect_right(A, x))
