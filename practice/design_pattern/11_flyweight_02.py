# Flyweight

class FlyweightMixin:
    _instances = {}

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if (cls, *args) not in cls._instances:
            # print(*args)
            # for k, v in kwargs.items():
            #     print(k, v)
            new_instance = cls(**kwargs)
            cls._instances[(cls, *args)] = new_instance
            return new_instance
        else:
            return cls._instances.get((cls, *args))

class User(FlyweightMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Car(FlyweightMixin):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

user1 = User.get_instance(1, name='Taro', age=21)
user2 = User.get_instance(1)
print(id(user1), id(user2))

car1 = Car.get_instance(1, brand='TOYOTA', model='Prius')
print(car1.brand)
