# Typical001A
from collections import deque

def print_graph(gh):
    for g in gh:
        print(g)

h, w = map(int, input().split())

# print(h, w)

c_hw = []
for i in range(h):
    cc = input()
    c_hw.append(cc)

    s = cc.find('s')
    if s != -1:
        sy = i
        sx = s
    g = cc.find('g')
    if g != -1:
        gy = i
        gx = g

# print(sy, sx)
# print(gy, gx)

# print_graph(c_hw)

dist = [[-1] * w for x in range(h)]
dist[sy][sx] = 0

# print_graph(dist)

dq = deque()
dq.append([sy, sx])

left = [-1, 0]
right = [1, 0]
up = [0, -1]
down = [0, 1]
ops = [left, up, right, down]

while dq:
    vy, vx = dq.pop()

    for op in ops:
        t_vy = vy
        t_vx = vx

        t_vy += op[0]
        t_vx += op[1]

        # 範囲外
        if t_vy < 0 \
            or t_vy >= h \
            or t_vx < 0 \
            or t_vx >= w:
            continue

        # 通行できない
        if c_hw[t_vy][t_vx] == '#':
            continue

        # 探索済み
        if dist[t_vy][t_vx] != -1:
            continue

        # print(t_vy, t_vx)
        dist[t_vy][t_vx] = dist[vy][vx] + 1
        dq.append([t_vy, t_vx])

        # ゴールに到達した
        if t_vy == gy and t_vx == gx:
            # print_graph(dist)
            dq.clear()
            break

if dist[gy][gx] == -1:
    print('No')
else:
    print('Yes')
