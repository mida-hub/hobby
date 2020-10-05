# リコリフの置換原則

# 長方形
class Rectangle:
  def __init__(self, width, height):
    self._width = width
    self._height = height

  @property
  def width(self):
    return self._width

  @width.setter
  def width(self, value):
    self._width = value

  @property
  def height(self):
    return self._height

  @height.setter
  def height(self, value):
    self._height = value

  def calcurate_area(self):
    return self.width * self.height

class Square(Rectangle):
  # NG
  # def __init__(self, size):
  #   self.size = size
  
  # def calcurate_area(self):
  #   return self.size * self.size

  def __init__(self, size):
    self._width = size
    self._height = size
  
  @Rectangle.width.setter
  def width(self, size):
    self._width = size
    self._height = size

  @Rectangle.height.setter
  def height(self, size):
    self._width = size
    self._height = size

  def calcurate_area(self):
    return self._width * self._height

def print_area(obj, height):
  obj.height = height
  print(f'予想 = {obj.width * height}, 実際 = {obj.width * obj.height}')

rc = Rectangle(2, 3)
print_area(rc, 10)

sq = Square(5)
print_area(sq, 10)

