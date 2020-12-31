from collections import deque

# deque vs list
q = deque([1, 2, 3 ,4])
# q = [1, 2, 3, 4]

# deque 挙動確認
# print(q.pop())
# print(q.popleft())
# q.append(5)
# q.appendleft(10)
# print(q)
# print(list(q))

from time import time

start_time = time()
print('-'*50)
LOOP_COUNT = 5000000
for x in range(LOOP_COUNT):
    q.append(x)
mid_time = time()
print(f'append time ({mid_time - start_time})')

for _ in range(LOOP_COUNT):
    tmp = q.pop()
pop_time = time()
print(f'pop time ({pop_time - mid_time})')

for x in range(LOOP_COUNT):
    q.insert(x, x)
end_time = time()
print(f'insert time ({end_time - pop_time})')