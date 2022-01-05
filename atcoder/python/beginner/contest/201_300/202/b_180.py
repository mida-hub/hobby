convert_dict = {
    '0': '0',
    '1': '1',
    '6': '9',
    '8': '8',
    '9': '6'
}

S = input()
convert_s = ''

for s in reversed(S):
    # print(s)
    convert_s += convert_dict[s]
print(convert_s)
