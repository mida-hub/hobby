from collections import namedtuple

S = namedtuple('Student', ['name', 'age', 'grade'])
taro = S('Taro', 12, 3)
print(taro.name)
print(taro)
taro = taro._replace(name='Jiro')
print(taro)
print(taro._asdict())
print(taro._fields)

dict_b = {'name': 'John', 'age': 20, 'grade': 2}
john = S(**dict_b)
print(john)

paul = S._make(['Paul', 15, 2])
print(paul)