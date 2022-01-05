def main():
    from decimal import Decimal
    import math
    x, y, r = map(Decimal, input().split())

    start = math.ceil(x-r)
    end = math.floor(x+r)

    total = 0
    for i in range(start, end+1):
        p = (r * r - (x - i) ** 2).sqrt()
        bottom = math.ceil(y-p)
        top = math.floor(y+p)
        
        total+=(top-bottom+1)

    print(total)

main()
