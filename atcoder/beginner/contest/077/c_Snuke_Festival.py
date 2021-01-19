def main():
    def meguru_bisect(left, right, func):
        while (abs(right - left) > 1):
            mid = (right + left) // 2
            # print(f'right:{right}')
            # print(f'left:{left}')
            # print(f'mid:{mid}')
            # print('-'*10)
            if func(mid):
                right = mid
            else:
                left = mid
        return right

    def bisect_left(arr, x):
        def func(i):
            return x <= arr[i]
        return meguru_bisect(-1, len(arr), func)

    def bisect_right(arr, x):
        def func(i):
            return x < arr[i]
        return meguru_bisect(-1, len(arr), func)

    n = int(input())
    an = sorted(list(map(int, input().split())))
    bn = sorted(list(map(int, input().split())))
    cn = sorted(list(map(int, input().split())))

    # print(an, bn, cn)
    total = 0
    for b in bn:
        b_left_a = bisect_left(an, b)
        b_right_c = len(cn) - bisect_right(cn, b)
        total += b_left_a * b_right_c

        # print(f'b:{b}')
        # print(b_left_a)
        # print(b_right_c)
        # print('-'*20)

    print(total)

main()
