
from abc import abstractclassmethod, ABCMeta

class Human(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
    
    @abstractclassmethod
    def say_somothing(self):
        pass

    def say_name(self):
        print(self.name)
    
class Woman(Human):
    def say_somothing(self):
        print(f'女性: 名前は{self.name}')

class Man(Human):
    def say_somothing(self):
        print(f'男性: 名前は{self.name}')

num = input('input 0 or 1:')
if num == '0':
    human = Man('Taro')
elif num == '1':
    human = Woman('Hanako')
else:
    print('input miss!')

human.say_somothing()