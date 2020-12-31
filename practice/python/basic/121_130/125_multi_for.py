import itertools

all_nums_iter = itertools.product(range(10),repeat=3)

result = []
for i, j, k in all_nums_iter:
    summed = i*100 + j*10 + k
    # print(i, j, k)
    if i == j == k and summed >= 500:
        result.append(summed)
        break
print(result)
