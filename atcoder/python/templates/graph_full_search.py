#!/usr/bin/env python3
# abc232c
import sys
import itertools

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, M: int, A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]"):
    ab_matrix = [[False] * N for x in range(N)]
    cd_matrix = [[False] * N for x in range(N)]

    for a, b in zip(A, B):
        ab_matrix[a-1][b-1] = True
        ab_matrix[b-1][a-1] = True
    for c, d in zip(C, D):
        cd_matrix[c-1][d-1] = True
        cd_matrix[d-1][c-1] = True

    # print(ab_matrix)
    # print(cd_matrix)

    for perm in itertools.permutations(range(N), N):
        # print(perm)
        ans = True
        for i in range(N):
            for j in range(N):
                # print(f"i,j,perm[i],perm[j]:{i+1},{j+1},{perm[i]+1},{perm[j]+1}={ab_matrix[i][j] == cd_matrix[perm[i]][perm[j]]}")
                if ab_matrix[i][j] != cd_matrix[perm[i]][perm[j]]:
                    ans = False
        if ans:
            print(YES)
            return
    print(NO)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    C = [int()] * (M)  # type: "List[int]"
    D = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(N, M, A, B, C, D)

if __name__ == '__main__':
    main()