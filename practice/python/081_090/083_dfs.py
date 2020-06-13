W, H = None, None
S = None
Sh, Sw, Gh, Gw = None, None, None, None
reached = None

def search(x, y):
    global reached
    # 迷路の外か壁
    if x < 0 or H <= x or y < 0 or W <= y or S[x][y] == '#': return
    # 以前に到達している場合
    if reached[x][y]: return None
    
    # 探索済みフラグ
    reached[x][y] = True

    # 到達できた
    if x == Gh and y == Gw:
        # print(x, y)
        return

    search(x + 1, y    )
    search(x - 1, y    )
    search(x    , y + 1)
    search(x    , y - 1)

    return

def get_start_point_and_goal_point(H, W, S):
    Sh = None
    Sw = None
    Gh = None
    Gw = None

    for hi in range(H):
        for wi in range(W):
            if S[hi][wi] == 's':
                Sh = hi
                Sw = wi
            if S[hi][wi] == 'g':
                Gh = hi
                Gw = wi
            
            if Sh is not None and Sw is not None and\
               Gh is not None and Gw is not None:
               return Sh, Sw, Gh, Gw

def deep_first_search(pH, pW, pS):
    """
    H: 高さ
    W: 幅
    S: 文字列のリスト
    """
    global H ,W, S
    global Sh, Sw, Gh, Gw
    global reached

    H = pH
    W = pW
    S = pS

    # スタートとゴールの座標を取得
    Sh, Sw, Gh, Gw = get_start_point_and_goal_point(H, W, S)
    
    # マッピング用フラグ初期化
    reached = [[False for i in range(W)] for j in range(H)]
    # 探索
    search(Sh, Sw)

    if reached[Gh][Gw]:
        print('Yes')
    else:
        print('No')

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