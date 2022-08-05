#!/usr/bin/env python3
import sys

def solve(N: int):
    ans = 0

    for i in range(1, N+1):
        k = i
        # print(f"k={k}")
        for d in range(2, k):
            if d * d > k:
                break
            # print(f"d={d}")
            while k % (d * d) == 0:
                # print(f"k={k}")
                k //= d * d
                # print(f"k={k}")
        for d in range(1, N+1):
            if k * d * d > N:
                break
            ans += 1
        # print(ans)
        # print('-'*50)
    print(ans)
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