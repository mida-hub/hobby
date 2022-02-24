#!/usr/bin/env python3
import re
import sys

def solve(A: int, B: int, X: int):
    def is_ok(arg):
        if A * arg + B * len(str(arg)) <= X:
            return True
        else:
            return False

    def meguru_bisect(ng, ok):
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid

        return ok

    print(meguru_bisect(ng=1000000000+1, ok=0))
    return

# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    solve(A, B, X)

if __name__ == '__main__':
    main()
