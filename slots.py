# import sys


# # slots

# # class Person:
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age

# # p = Person("James", 24)
# # print(p.__dict__)
# # p.x = 23
# # print(sys.getsizeof(p.__dict__) * 10000 / 1024, 'Kb')



# # class Person:
# #   __slots__ = ('name', 'age', 'hobby')
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age

# # p = Person("James", 24)
# # # print(p.__dict__)
# # print(sys.getsizeof(p.__slots__) * 10000 / 1024, 'Kb')
# # p.hobby = 'dev'


# class Location:
#   __slots__ = 'name', '__longitude', '__latitude'

#   def __init__(self, name, *, longitude, latitude):
#     self.name = name
#     self.__longitude = longitude
#     self.__latitude = latitude

#   @property
#   def longitude(self):
#     return self.__longitude
  
#   @property
#   def latitude(self):
#     return self.__latitude
  


# class Person:
#   __slots__ = '__name'

#   def __init__(self, name):
#     self.name = name

#   @property
#   def name(self):
#     return self.__name
  
#   @name.setter
#   def name(self, value):
#     if not isinstance(value, str) or value == "":
#       raise ValueError("String")
#     self.__name = value


# class Student(Person):
#   __slots__ = 'age'
#   def __init__(self, name, age):
#     super().__init__(name)
#     self.age = age
  


# # p = Person("")

# s = Student("James", 23)

# # print(p.name)
# print(s.__dict__)


# Descriptors

class Point2D:
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  @property
  def x(self):
    return self.__x
  
  @x.setter
  def x(self, value):
    if value < 0: 
      raise ValueError('Value must be grather than 0')
    self.__x = value

  @property
  def y(self):
    return self.__y
  
  @y.setter
  def y(self, value):
    if value < 0: 
      raise ValueError('Value must be grather than 0')
    self.__y = value


p = Point2D(2, 3)
# print(p.x)
# print(Point2D.x)
# __get__, __set__

class IntegerValue:
  def __get__(self, instance, owner):
    if instance is None:
      return self
    # print(f"self - {hex(id(self))}, instance - {hex(id(instance))},  owner - {hex(id(owner))}")

  def __set__(self, instance, value):
    print(f"self={self}, instance={instance}, value={value}")



class Point2D:
  
  x = IntegerValue()
  # print(f"Descriptori hasce {hex(id(x))}")





# p1 = Point2D()
print(Point2D.x)
# print(f"p1 i hasce {hex(id(p1))}")
# print(f"Point2D classi hasce {hex(id(Point2D))}")

