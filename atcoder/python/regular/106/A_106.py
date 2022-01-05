n = int(input())

a = 3
b = 5

is_exist = False
answer_i = -1
answer_j = -1
for i in range(1, 50):
    for j in range(1, 40):
        # print(i, j)
        ab = a ** i + b ** j
        # print(ab)
        # if ab > n:
        #     break
        if ab == n:
            is_exist = True
            answer_i = i
            answer_j = j

if is_exist:
    print(answer_i, answer_j)
else:
    print(-1)
