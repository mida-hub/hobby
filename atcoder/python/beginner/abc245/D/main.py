#!/usr/bin/env python3
import sys
from numpy import poly1d

def solve1(N: int, M: int, A: "List[int]", C: "List[int]"):
    B = [0] * (M + 1)
    for i in reversed(range(M+1)):
        B[i] = C[i + N] // A[N]
        for j in range(N):
            C[i + j] -= B[i] * A[j]

    print(' '.join(map(str, B)))
    
    return

def solve2(N: int, M: int, A: "List[int]", C: "List[int]"):
    polyA = poly1d(list(reversed(A)))
    polyC = poly1d(list(reversed(C)))

    polyB = polyC / polyA
    # print(polyB)
    print(' '.join(map(str, map(int, reversed(polyB[0].c)))))

# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N + 1)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(N + M + 1)]  # type: "List[int]"
    solve1(N, M, A, C)
    # solve2(N, M, A, C)

if __name__ == '__main__':
    main()
