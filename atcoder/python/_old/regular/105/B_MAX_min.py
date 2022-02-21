n = int(input())
an = list(map(int, input().split()))

import math
from functools import reduce
def gcd_list(numbers):
    return reduce(math.gcd, numbers)
print(gcd_list(an))

# while True:
#   a_min = min(an)
#   a_max = max(an)
#   if a_min == a_max:
#     print(a_min)
#     break
#   else:
#     an = [a_max - a_min if a == a_max else a for a in an]
#   print(an)
