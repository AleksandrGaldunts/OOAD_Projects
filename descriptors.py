import weakref

class ValidString:
  def __init__(self):
    self.value = weakref.WeakKeyDictionary()

  def __get__(self, instance, owner):
    if instance is None:
      return self
    return self.value.get(instance, "Non-value")

  def __set__(self, instance, value):
    if not isinstance(value, str):
      raise ValueError("value must be a string")
    self.value[instance] = value


class User:
  first_name = ValidString()
  last_name = ValidString()


u1 = User()

print(u1.first_name)
u1.first_name = "James"
print(u1.first_name)

print(User.first_name.value)

u2 = User()
u2.first_name = "Bob"
print(u1.first_name, u2.first_name)
print(User.first_name.value)
u1.last_name = "Smith"
print(u1.first_name)

del u1

print(User.first_name.value)

u1 = User()

u1.first_name = "James"

print(hex(id(u1)))
# del u1

print(User.first_name.value)

# import ctypes


# def ref_count(address):
#   print(ctypes.c_long.from_address(address).value)

# # u1_id = id(u1)

# # del u1

# # ref_count(u1_id)


# class Person:
#   pass

# p1 = Person()

# p1_id = id(p1)



# import weakref

# weak_p3 = weakref.ref(p1)
# print(p1)
# ref_count(p1_id)
# print(weak_p3())

# p4 = weak_p3()
# ref_count(p1_id)


# class IntegerValue:
#   def __init__(self, name):
#     self.name = "_" + name

#   def __set__(self, instance, value):
#     if not isinstance(value, int):
#       raise ValueError("bla bla")
#     # setattr(instance, self.name, value)
#     instance.__dict__[self.name] = value
  
#   def __get__(self, instance, owner):
#     if instance is None:
#       return self
      
#     return getattr(instance, self.name)
  

# class Vector:
#   x = IntegerValue('x')

#   def __init__(self, value):
#     self.x = value


# v1 = Vector("Hello")
# print(v1.x)


# class StringValue:
#   def __set_name__(self, owner, property_name):
#     self.property_name = "__" + property_name
#
#   def __get__(self, instance, owner):
#     if instance is None:
#       return self
#     return getattr(instance, self.property_name, None)
#
#   def __set__(self, instance, value):
#     if not isinstance(value, str):
#       raise ValueError("value must be a string")
#     setattr(instance, self.property_name, value)
#     # instance.__dict__[self.property_name] = value
#
#   def __delete__(self, instance):
#     del instance.get(self.property_name)
#
#
# class User:
#   first_name = StringValue()
#   last_name = StringValue()
#   email = StringValue()
#
# user1 = User()
# user1.first_name = "Bob"
# user1.last_name = "Smith"
# user1.email = "example@gmail.com"
#
# print(user1.__dict__)
















