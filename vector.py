# from numbers import Real
# from typing import Sequence, Sized, Container, Mapping, Iterable
#
# class Vector:
#   def __init__(self, *components):
#     if len(components) < 1:
#       raise ValueError("Can't be empty")
#     self.__components = tuple(components)
#
#   @property
#   def components(self):
#     return self.__components
#
#   def __len__(self):
#     return len(self.components)
#
#   def __repr__(self) -> str:
#     return f"Vector{self.components}"
#
#   def validate_type_and_dimension(self, v):
#     return len(v) == len(self)
#
#   def __add__(self, other):
#     if not self.validate_type_and_dimension(other):
#       return NotImplemented
#
#     if isinstance(other, Sequence):
#       other = Vector(*other)
#     components = (x + y for x, y in zip(self.components, other.components))
#     return Vector(*components)
#
#   # def __radd__(self, other):
#   #   return self + other
#
# # in-place addition
# # sub, mul, div, abs, pos, neg
#   # def __iadd__(self, other):
#
#   #   self = self + other
#   #   return self
#
#
# v1 = Vector(1, 2)
# v2 = Vector(5, 5)
#
#
# # v1 += v2
#
# # print((1, 3) + v1)
#
#
#
# class Person:
#   def __init__(self, age):
#     self.__age = age
#
#   @property
#   def age(self):
#     return self.__age
#
#   def __eq__(self, other):
#     return self.age == other.age
#
#   def __hash__(self):
#     return hash(self.__age)
#
#   def __repr__(self):
#     return f'Person-ի age-ը {self.__age}'
#
#
#
#
# p1 = Person(13)
# p2 = Person(13)
#
# # print(dir(object))
# # print(id(p1))
# # print(hash(p1))
#
# # print(p1 == p2)
# # di = {p1: 'James'}
# # p1.age = 563
#
# # print(di[p1])


class Person:
  def __len__(self):
    return 1
  
  def __bool__(self):
    return False

# print(help(Sized))
p1 = Person()
print(Person.__mro__)
#print(isinstance(p1, Sized))
print(bool(Person))




