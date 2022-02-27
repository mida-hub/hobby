from functools import reduce

def gcd(x, y):
    if y == 0:
        return x 
    else:
        return gcd(y, x%y)

# 最大公約数
def gcd_list(num_list: list) -> int:
    return reduce(gcd, num_list)

print(gcd_list([12, 15, 24]))
