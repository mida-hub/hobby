n, k = map(int, input().split())
an = list(map(int, input().split()))
an_copy = an.copy()
an_copy.sort()
an_dict = {}

for i, a in enumerate(an_copy):
    an_dict[a] = i+1

# print(an_dict)

k_div_n = k // n 
k_mod_n = k % n
# print(k_div_n)
# print(k_mod_n)

for a in an:
    if an_dict[a] <= k_mod_n:
        print(k_div_n+1)
    else:
        print(k_div_n)
