from functools import reduce

def gcd(x, y):
    if y == 0:
        return x 
    else:
        return gcd(y, x%y)

def lcm_base(x: int, y: int) -> int:
    return (x * y) // gcd(x, y)

def lcm_list(num_list: list):
    return reduce(lcm_base, num_list, 1)

print(lcm_list([3, 4, 15]))
