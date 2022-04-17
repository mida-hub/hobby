#!/usr/bin/env python3
import sys


def solve(N: int):
    s = []
    s.append('0')
    s.append('1')

    for n in range(2, N+1):
        s.append(f'{s[n-1]}+{n}+{s[n-1]}')

    print(s[N].replace('+', ' '))

    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
