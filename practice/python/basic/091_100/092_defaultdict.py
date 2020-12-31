from collections import defaultdict

d_dict_str = defaultdict(str)
print(d_dict_str['A'])
print(type(d_dict_str['A']))
d_dict_str['A'] = 100
print(d_dict_str['A'])

print('-'*50)

d_dict_int = defaultdict(lambda: 1)
print(d_dict_int['A'])
print(type(d_dict_int['A']))
d_dict_int['A'] = 100
print(d_dict_int['A'])
d_dict_int['B'] += 1
print(d_dict_int)
print(d_dict_int.keys(), d_dict_int.values())