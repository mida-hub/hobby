#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(N: int, A: "List[int]"):
    total = 0
    sn = [0]
    for i, ai in enumerate(reversed(A)):
        sn.append(sn[i] + ai)
        total += sn[i] * ai 
        total %= MOD

        # print(f'ai={ai}')
        # print(f'sn={sn}')
        # print(f'total={total}')
    print(total)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
