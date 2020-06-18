from collections import Counter
from random import randint, seed

seed(1)

list_a = [randint(0, 10) for _ in range(100)]

cnt = Counter(list_a)

# print(sorted(list_a))
print(cnt)
# print(cnt[0])
# print(list(cnt.elements()))
# print(cnt.most_common())

# cnt.subtract({7:20, 6:-5})
# print(cnt.most_common())