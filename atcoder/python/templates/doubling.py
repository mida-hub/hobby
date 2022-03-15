#!/usr/bin/env python3
# abc167d
import sys


def solve(N: int, K: int, A: "List[int]"):
    logk = K.bit_length()
    doubling = [[] * N for _ in range(logk)]

    # 前処理    
    for j in range(N):
        doubling[0].append(A[j] - 1)
    # print(doubling)

    for i in range(1, logk):
        for j in range(N):
            doubling[i].append(doubling[i-1][doubling[i-1][j]])
        # print(doubling)

    # K を 2進数展開して、 1 のときに計算する 
    now = 0
    for i in range(logk):
        # print(i, K, end=" ")
        if K & 1:
            # print(now, end=" -> ")
            now = doubling[i][now]
            # print(now)
        # else:
        #     print()
        K = K >> 1
    print(now + 1)

    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)

if __name__ == '__main__':
    main()
