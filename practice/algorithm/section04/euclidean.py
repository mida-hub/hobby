
def gcd(m, n):
    if n == 0:
        return m
    
    return gcd(n, m % n)

print(gcd(51, 15))
print(gcd(15, 51))
