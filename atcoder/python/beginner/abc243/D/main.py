#!/usr/bin/env python3
import sys


def main():
    N, X = map(int, input().split())
    S0 = input()
    S = []

    # RU LU みたいな操作を打ち消す
    for s0 in S0:
        # print(s0)
        if s0 == 'U' and len(S) > 0 and S[len(S) - 1] != 'U':
            S.pop()
        else:
            S.append(s0)
    # print(X)
    # print(S)

    for s in S:
        if s == 'U':
            X = X // 2
        elif s == 'L':
            X = X * 2
        elif s == 'R':
            X = X * 2 + 1
        # print(X)
    print(X)

if __name__ == '__main__':
    main()
