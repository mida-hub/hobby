n = 2

for i in range(2 ** n):
    # フラグ作成
    for j in range(n):
        if ((i >> j) & 1):
            print(i, j, end=" ")
    print()

print("this means is")
print("1, 0")
print("0, 1")
print("1, 1")
