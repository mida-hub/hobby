def make_divisors(n: int) -> list:
    return_list = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            return_list.append(i)
            if i != n // i:
                return_list.append(n//i)

    return return_list

print(make_divisors(10))
print(make_divisors(25))
print(make_divisors(31))
print(make_divisors(655))
