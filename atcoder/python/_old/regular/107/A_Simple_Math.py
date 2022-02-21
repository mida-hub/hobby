a, b, c = map(int, input().split())
m = 998244353
wa = (a * a + a) * (b * b + b) * (c * c + c) // 8
wa = wa % m
print(wa)
