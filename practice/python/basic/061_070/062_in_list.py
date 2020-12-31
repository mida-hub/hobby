value = [x for x in range(10)]
print(value)

value = [x * x for x in range(10) if x % 2 == 0]
print(value)

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        else:
            return True

list_prime = [x for x in range(2, 100) if is_prime(x) == True]
print(list_prime)
