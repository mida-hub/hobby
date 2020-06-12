
class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        print('getter name が呼ばれました')
        return self.__name
    
    @property
    def age(self):
        print('getter age が呼ばれました')
        return self.__age

    @name.setter
    def name(self, name):
        print('setter name が呼ばれました')
        self.__name = name

    @age.setter
    def age(self, age):
        print('setter age が呼ばれました')
        if age < 0:
            print('0以上の値を設定してください')
            return
        self.__age = age

human = Human('koichi', 22)
print(human.name)
print(human.age)
human.name = 'Makoto'
human.age = -1
human.age = 3
print(human.age)
