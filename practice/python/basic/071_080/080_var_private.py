
class Human:
    __class_val = 'Human'

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def print_msg(self):
        print(f'name = {self.__name}, age = {self.__age}')

human = Human('Taro', 15)
# プライベート変数なのでアクセスできない
# print(human.__name)

# ただし、この記法を使うとアクセスできる
# print(human._Human__name)

human.print_msg()