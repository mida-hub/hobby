
class Human:

    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number
    
    def __str__(self):
        return self.name + ',' + str(self.age) + ',' + self.phone_number

    def __eq__(self, other):
        return (self.name == other.name) and (self.phone_number == other.phone_number)

    def __hash__(self):
        return hash(self.name + self.phone_number)

    def __bool__(self):
        return True if self.age >= 20 else False

    def __len__(self):
        return len(self.name)

man1 = Human('Taro', 20, '08011112222')
man2 = Human('Taro', 18, '08011112222')
man3 = Human('JiroW', 18, '09011112222')

print(man1)
print(man1 == man2)

set_men = {man1, man2, man3}

for x in set_men:
    print(x)

if man1:
    print('man1 は True')

if man2:
    print('man2 は True')

print(len(man1))
print(len(man2))
print(len(man3))
