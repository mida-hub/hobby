class UserInfo:
    def __init__(self, name, age, phone_number):
      self.name = name
      self.age = age
      self.phone_number = phone_number

    def __str__(self):
      return f'{self.name}, {self.age}, {self.phone_number}'

    # NG
    # def write_str_to_file(self, filename):
    #   with open(filename, mode='w') as f:
    #     f.write(str(self))

class Company:
    pass

class FileManager:

    @staticmethod
    def write_str_to_file(obj, filename):
      with open(filename, mode='w') as f:
        f.write(str(obj))

user_info = UserInfo('taro', 21, '090-1234-5678')
print(user_info)
# user_info.write_str_to_file('tmp.txt')
FileManager.write_str_to_file(user_info, 'tmp2.txt')
