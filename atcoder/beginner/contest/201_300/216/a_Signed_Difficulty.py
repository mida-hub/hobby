xy = input()

x, y = xy.split('.')
# print(x, y)
y = int(y)

if 0 <= y <= 2:
    print(x + '-')
elif 3 <= y <= 6:
    print(x)
elif 7 <= y <= 9:
    print(x + '+')
