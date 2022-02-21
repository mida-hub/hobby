n = int(input())
s = input()

# print(n)
# print(s)

index = n-3
# index = n-4
while index >= 0:
    # print('-'*10)

    # print(s[index:index+3])
    if s[index:index+3] == 'fox':
        s = s[:index] + s[index+3:]
    # print(s)
    index -= 1
    # print(index)

print(len(s))
