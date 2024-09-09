# # 1. type returns type of instance or class
# import math
# class Person:
#   pass


# # 2.type -> returns new class

# class Circle:
#   def __init__(self, x, y, r):
#     self.x = x
#     self.y = y 
#     self.r = r
  
#   def area(self):
#     return self.r * math.pi ** 2
# namespace = {}
# exec('''
# x = 10
# y = 20
# def __init__(self):
#   print(self)
# ''', globals(), namespace)

class_body = """
def __init__(self, x, y, r):
  self.x = x
  self.y = y
  self.r = r

def area(self):
  return self.r * math.pi ** 2
"""

class_dict = {}

exec(class_body, globals(), class_dict)

# Circle2 = type('Circle2', (object,), class_dict)

# c = Circle2(1, 2, 3)

# print(type)

# class Meta(type):
#   def __new__(mcls, name, bases, cls_dict):
#     print('hello our custom type')
#     return super().__new__(mcls, name, bases, class_dict)
  
# class Person(object):
#   def __new__(cls, *args, **kwargs):
#     print(args)
#     return super().__new__(cls)

#   def __init__(self, a, b):
#     print('__init__')

# p = Person.__new__(Person, 1, 2)
# p.__init__(1, 2)

# # x = Person()

class Meta(type):
  def __new__(mcls, name, bases, cls_dict):
    cls_dict['custom_method'] = lambda x: x + 1
    # print('Meta.__new__ called...')
    # print('\tmcls:', mcls)
    # print('\tname:', name)
    # print('\tbases:', bases)
    # print('\tcls_dict:', cls_dict)

    return super().__new__(mcls, name, bases, cls_dict)
  
class X(metaclass=Meta):
  pass


class Metaclass():

  def __new__(cls, name, bases, cls_dict, **kwargs):
    print('__new__')
    print(cls_dict)
    print(kwargs)
    return super().__new__(cls, name, bases, cls_dict)

  @staticmethod
  def __prepare__(name, bases, **kwargs):
    kwargs.update({'a': 34})
    print('Metaclass.__prepare__ called...')
    print('name: ', name)
    print('bases: ', bases)
    print('kwargs: ', kwargs)
    return kwargs

class A(metaclass=Metaclass):
  pass

