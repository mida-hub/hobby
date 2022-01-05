a, b, c = map(int, input().split())
is_even = True if c % 2 == 0 else False

if is_even and (abs(a) == abs(b)):
    print('=')
elif is_even and (abs(a) > abs(b)):
    print('>')
elif is_even and (abs(a) < abs(b)):
    print('<')
elif not is_even and (a == b):
    print('=')
elif not is_even and (a > b):
    print('>')
elif not is_even and (a < b):
    print('<')
