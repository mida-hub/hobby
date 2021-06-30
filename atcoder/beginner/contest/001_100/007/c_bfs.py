from collections import deque

def print_graph(gh):
    for g in gh:
        print(g)

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

# 0始まりに合わせる
sy -= 1
sx -= 1
gy -= 1
gx -= 1

c_rc = []
for i in range(r):
    cc = input()
    c_rc.append(cc)

# print_graph(c_rc)

dist = [[-1] * c for x in range(r)]
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
    vy, vx = dq.popleft()

    for op in ops:
        t_vy = vy
        t_vx = vx

        t_vy += op[0]
        t_vx += op[1]

        # 範囲外
        if t_vy < 0 \
            or t_vy >= r \
            or t_vx < 0 \
            or t_vx >= c:
            continue

        # 通行できない
        if c_rc[t_vy][t_vx] == '#':
            continue

        # 探索済み
        if dist[t_vy][t_vx] != -1:
            continue

        # print(t_vy, t_vx)
        dist[t_vy][t_vx] = dist[vy][vx] + 1
        dq.append([t_vy, t_vx])

# print_graph(dist)
print(dist[gy][gx])
