
def deep_first_search(H, W, S):
    """
    H: 高さ
    W: 幅
    S: 文字列のリスト
    """

    def search(x, y):
        # 迷路の外か壁
        if x < 0 or H <= x or y < 0 or W <= y or S[x][y] == '#': return False
        # 以前に到達している場合
        if reached[x][y]: return False
        
        # 探索済みフラグ
        reached[x][y] = True

        # 到達できた
        if S[x][y] == 'g':
            # print(x, y)
            return True

        return search(x + 1, y    ) | \
               search(x - 1, y    ) | \
               search(x    , y + 1) | \
               search(x    , y - 1)

    # マッピング用フラグ初期化
    reached = [[False for i in range(W)] for j in range(H)]
    
    for hi in range(H):
        for wi in range(W):
            if S[hi][wi] == 's':
                # 探索
                if search(hi, wi):
                    print('Yes')
                else:
                    print('No')
                return

Hs = [4, 4, 10, 10, 1]
Ws = [5, 4, 10, 10, 10]
spots = [
    ['s####', '....#', '#####', '#...g'],
    ['...s', '....', '....', '.g..'],
    ['s.........', '#########.', '#.......#.', '#..####.#.', '##....#.#.', '#####.#.#.', 'g.#.#.#.#.', '#.#.#.#.#.', '###.#.#.#.', '#.....#...'],
    ['s.........', '#########.', '#.......#.', '#..####.#.', '##....#.#.', '#####.#.#.', 'g.#.#.#.#.', '#.#.#.#.#.', '#.#.#.#.#.', '#.....#...'],
    ['s..####..g']
]
deep_first_search(Hs[0], Ws[0], spots[0]) # Noと表示
deep_first_search(Hs[1], Ws[1], spots[1]) # Yesと表示
deep_first_search(Hs[2], Ws[2], spots[2]) # Noと表示
deep_first_search(Hs[3], Ws[3], spots[3]) # Yesと表示
deep_first_search(Hs[4], Ws[4], spots[4]) # Noと表示