# i = 5
# print(bin(i))
# print(bin(i >> 2))
# print((i >> 2) & 1)

money = 300
item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
n = len(item)
for i in range(2 ** n):
    bag = []
    print("pattern {}: ".format(i), end="")
    for j in range(n):  # このループが一番のポイント
        # print(i, j, bin(i >> j))
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            bag.append(item[j][0])  # フラグが立っていたら bag に果物を詰める
    print(bag)