#!/usr/bin/env python3
from collections import deque

def main():
    deq = deque()

    Q = int(input())

    for _ in range(Q):
        q = list(map(int, input().split()))
        # print(q)
        if q[0] == 1:
            deq.append([q[1], q[2]])
        else:
            c = q[1]
            total = 0
            while True:
                d = deq.popleft()
                c_x = d[0]
                c_d = d[1]
                
                if c_d - c > 0:
                    total += c_x * c
                    print(total)
                    deq.appendleft([c_x, c_d - c])
                    break
                elif c_d == c:
                    total += c_x * c
                    print(total)
                    break
                else:
                    total += c_x * c_d
                    c -= c_d
        # print(deq)

if __name__ == '__main__':
    main()
