
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print(f'hello {self.name}')

    def say_age(self):
        print(f'{self.age} years old')

class Employee(Person):

    def __init__(self, name, age, number):
        super().__init__(name, age)
        self.number = number
    
    def say_number(self):
        print(f'my number is = {self.number}')

    def greeting(self): # override
        super().greeting()
        print(f'I\'m employee phone_number = {self.number}')

man = Employee('Tonegawa', 45, '08011112222')
man.greeting()
man.say_age()
man.say_number()