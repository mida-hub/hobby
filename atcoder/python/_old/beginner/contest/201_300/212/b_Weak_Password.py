x = input()
x1, x2, x3, x4 = map(int, list(x))

# print(x1, x2, x3, x4)

if x1 == x2 == x3 == x4:
    print('Weak')
elif x4 == (x3+1)%10 and \
     x3 == (x2+1)%10 and \
     x2 == (x1+1)%10:
    print('Weak')
else:
    print('Strong')
