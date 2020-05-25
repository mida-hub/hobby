# バブルソート

list_a = [5,7,4,5,1,2,3,2,9,1,4]

for i in range(len(list_a)):
    for j in range(0, len(list_a) - i - 1):
        if list_a[j] > list_a[j + 1]:
            list_a[j], list_a[j + 1] = list_a[j + 1], list_a[j]
    print(list_a)

print(list_a)