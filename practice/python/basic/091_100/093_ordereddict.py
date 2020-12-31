from collections import OrderedDict

o_dict = OrderedDict([('A', 100), ('B', 200)])
print(o_dict['A'])
o_dict.move_to_end('B', False)
print(o_dict)

print({'A': 100, 'B': 200} == {'B': 200, 'A': 100})
print(([('A', 100), ('B', 200)]) == OrderedDict([('B', 200), ('A', 100)]))
