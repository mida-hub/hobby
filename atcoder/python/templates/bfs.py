#!/usr/bin/env python3
# abc007c
from collections import deque

# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    r, c = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    c_rc = []
    for ri in range(r):
        c_rc.append(list(input()))

    # print(r, c)
    # print(sy, sx)
    # print(gy, gx)
    # for rc in c_rc:
    #     print(rc)

    # 0はじまり
    sy -= 1
    sx -= 1
    gy -= 1
    gx -= 1

    dist = [[-1] * c for x in range(r)]
    dist[sy][sx] = 0

    left = [-1, 0]
    right = [1, 0]
    up = [0, -1]
    down = [0, 1]

    ops = [left, right, up, down]

    deq = deque()
    deq.append([sx, sy])

    while deq:
        d = deq.popleft()
        d_c = d[0]
        d_r = d[1]
        
        for op in ops:
            op_c = op[0]
            op_r = op[1]

            row = d_r + op_r
            col = d_c + op_c

            # 範囲外
            if row < 0 or r <= row or col < 0 or c <= col:
                continue
            
            # 壁
            if c_rc[row][col] == '#':
                continue

            # 探索済み
            if dist[row][col] != -1:
                continue
            
            dist[row][col] = dist[d_r][d_c] + 1
            deq.append([col, row])

    # for d in dist:
    #     print(d)
    print(dist[gy][gx])

if __name__ == '__main__':
    main()
