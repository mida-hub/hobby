from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    grade: int

taro = Student('Taro', 12, 3)
print(taro)
taro.grade = 4
print(taro)

# jiro = Student('Jiro', 12, 4)
jiro = Student('Taro', 12, 4)

print(taro==jiro)