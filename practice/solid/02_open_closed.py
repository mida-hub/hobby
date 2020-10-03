# 開放閉鎖の原則
from abc import ABCMeta, abstractmethod

class UserInfo:
  def __init__(self, name, job_name, nationality):
    self.name = name
    self.job_name = job_name
    self.nationality = nationality

  def __str__(self):
    return f'{self.name}, {self.job_name}, {self.nationality}'

class Comparation(metaclass=ABCMeta):
  @abstractmethod
  def is_equal(self, other):
    pass

  def __and__(self, other):
    return AndComparation(self, other)

  def __or__(self, other):
    return OrComparation(self, other)

class AndComparation(Comparation):
  def __init__(self, *args):
    self.comparations = args

  def is_equal(self, other):
    return all(
      map(
        lambda comparation: comparation.is_equal(other),
        self.comparations
      )
    )

class OrComparation(Comparation):
  def __init__(self, *args):
    self.comparations = args

  def is_equal(self, other):
    return any(
      map(
        lambda comparation: comparation.is_equal(other),
        self.comparations
      )
    )

class Filter(metaclass=ABCMeta):
  @abstractmethod
  def filter(self, comparation, items):
    pass

class JobNameComparation(Comparation):
  def __init__(self, job_name):
    self.job_name = job_name
  
  def is_equal(self, other):
    return self.job_name == other.job_name

class NationalityComparation(Comparation):
  def __init__(self, nationality):
    self.nationality = nationality
  
  def is_equal(self, other):
    return self.nationality == other.nationality 

class UserInfoFilter(Filter):
  def filter(self, comparation, items):
    for item in items:
      if comparation.is_equal(item):
        yield item

taro = UserInfo('taro', 'salary man', 'Japan')
jiro = UserInfo('jiro', 'police man', 'Japan')
john = UserInfo('john', 'salary man', 'USA')

user_list = [taro, jiro, john]
salary_man_comparation = JobNameComparation('salary man')
japan_comparation = NationalityComparation('Japan')
user_info_filter = UserInfoFilter()

for user in user_info_filter.filter(salary_man_comparation, user_list):
  print(user)

for user in user_info_filter.filter(japan_comparation, user_list):
  print(user)

print('-'*100)

salary_man_and_japan = salary_man_comparation & japan_comparation
for user in user_info_filter.filter(salary_man_and_japan, user_list):
  print(user)

print('-'*100)

salary_man_or_japan = salary_man_comparation | japan_comparation
for user in user_info_filter.filter(salary_man_or_japan, user_list):
  print(user)
