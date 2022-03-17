#!/usr/bin/env python3
# atc001b

YES = "Yes"
NO = "No"

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [i for i in range(n)]
        self.ranks = [0 for i in range(n)]
    
    # 根を探す
    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            # 経路圧縮 親に直接つなぎ直す 深さが3以上のときに有効
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # 同じグループに所属しているか判定する
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # 根を探した後に x -> y に統合する
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.parents[x] = y

    # 深さを見て、深いほうに統合する
    def unite_with_rank(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.ranks[x] < self.ranks[y]:
                self.parents[x] = y
            else:
                self.parents[y] = x
                if self.ranks[x] == self.ranks[y]:
                    self.ranks[x] += 1

    # 状態を表示する
    def __str__(self):
        return str(self.parents) + ' / ' + str(self.ranks)
        
def main():
    n, q = map(int, input().split())
    
    union_find = UnionFind(n)
    # print(f'n, q : {n}, {q}')
    # print(union_find)
    
    for i in range(q):
        p, a, b = map(int, input().split())
        # print(f'p, a, b : {p}, {a}, {b}')

        # 連結
        if p == 0:
            # union_find.unite(a, b)
            union_find.unite_with_rank(a, b)
        # 判定
        if p == 1:
            if union_find.same(a, b):
                print(YES)
            else:
                print(NO)

        # print(union_find)


if __name__ == '__main__':
    main()
