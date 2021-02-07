import math
x, y, r = map(float, input().split())
# print(x, y, r)

start = math.ceil(x-r)
end = math.floor(x+r)

total = 0
for i in range(start, end+1):
    p = (r * r - (x - i) ** 2) ** 0.5

    bottom = math.ceil(y-p)
    top = math.floor(y+p)

    total+=(top-bottom+1)

print(total)

