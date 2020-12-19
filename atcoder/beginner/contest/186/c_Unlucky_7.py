n = int(input())

seven = '7'
seven_list = []

for i in range(1, n+1):
    if seven in str(i):
        seven_list.append(i)
    if seven in '{:o}'.format(i):
        seven_list.append(i)

print(n - len(set(seven_list)))
