# # # # from typing import final
# # # #
# # # # @final
# # # # class MyBaseClass:
# # # #     # Class definition here
# # # #     pass
# # # #
# # # # class SubClass(MyBaseClass):
# # # #     # If you try to inherit from MyBaseClass,
# # # #     # mypy will raise an error because MyBaseClass is marked as final.
# # # #     pass
# #
# # def get_value(obj, key):
# #     if key in obj:
# #         return obj[key]
# #     elif 'parent' in obj:
# #         return get_value(obj['parent'], key)
# #     else:
# #         return None
# #
# #
# # def set_value(obj, key, value):
# #     obj[key] = value
# #
# #
# # # Base 'object' simulating a class
# # base_object = {
# #     'data': 'base data',
# #     'get_value': get_value,
# #     'set_value': set_value,
# # }
# #
# # # Derived 'object' that 'inherits' from base_object
# # derived_object = {
# #     'parent': base_object,  # This is how we simulate 'inheritance'
# #     'additional_data': 'derived data',
# #     'get_value': get_value,
# #     'set_value': set_value,
# # }
# #
# # # Accessing base 'class' data from the derived 'class'
# # print(derived_object['get_value'](derived_object, 'data'))  # Outputs 'base data'
# #
# # # Accessing derived 'class' data
# # print(derived_object['get_value'](derived_object, 'additional_data'))  # Outputs 'derived data'
# #
# #
# # class ClassMethod:
# #     def __init__(self, func):
# #         self.func = func
# #
# #     def __get__(self, instance, cls=None):
# #         if cls is None:
# #             cls = type(instance)
# #
# #         def wrapper(*args, **kwargs):
# #             return self.func(cls, *args, **kwargs)
# #
# #         return wrapper
# #
# #
# # #  Staticmethod
# #
# # class StaticMethod:
# #     def __init__(self, func):
# #         self.func = func
# #
# #     def __get__(self, instance, cls=None):
# #         return self.func
# #
# #
# # #
# # # class A:
# # #     def __init__(self):
# # #         self.b = None
# # #
# # # class B:
# # #     def __init__(self):
# # #         self.a = None
# # #
# # # a = A()
# # # b = B()
# # #
# # # a.b = b
# # # b.a = a
# #
# #
# # class MyMeta(type):
# #     def __call__(cls, *args, **kwargs):
# #         for attr in cls.__dict__.values():
# #             if hasattr(attr, '_isabstract') and attr.__dict__['_isabstract']:
# #                 raise ValueError
# #         return super().__call__(*args, **kwargs)
# #
# # def abstractmethod(foo):
# #     foo._isabstract = True
# #     return foo
# #
# # class A(metaclass=MyMeta):
# #     @abstractmethod
# #     def foo(self):
# #         ...
# # a = A()
# #
# #
# # # # with implemented
# #
# # # class File_Opener:
# # #     def __init__(self, filename, mode):
# # #         self.filename = filename
# # #         self.mode = mode
# # #         self.file = None
# # #     def __enter__(self):
# # #         self.file = open(self.filename, self.mode)
# # #         return self.file
# # #     def __exit__(self, exc_type, exc_val, exc_tb):
# # #         if self.file:
# # #             self.file.close()
# # #
# # # with File_Opener("File.txt", 'w') as  file:
# # #     file.write('wxw')
# #
# #
# # class ValidString:
# #     def __set_name__(self, owner, name):
# #         self.private_name = f"_{name}"
# #
# #     def __get__(self, instance, owner):
# #         return getattr(instance, self.private_name, "")
# #
# #
# #     def __set__(self, instance, value):
# #         print(instance)
# #         if not isinstance(value, str):
# #             raise ValueError("Assigned value must be a string")
# #         setattr(instance, self.private_name, value)
# #
# #     def __delete__(self, instance):
# #         delattr(instance, self.private_name)
# #
# # class MyClass:
# #     st = ValidString()
# #
# # # Usage
# # my_object = MyClass()
# # my_object.string = "Hello"
# # print(my_object.string)  # Outputs "Hello"
# #
# # try:
# #     my_object.string = 123  # Raises ValueError
# # except ValueError as e:
# #     print(e)
#
# #
# # class ValidString:
# #   def __set_name__(self, owner_class, property_name):
# #     self.property_name = property_name
# #
# #   def __set__(self, instance, value):
# #     instance.__dict__[self.property_name] = value
# #
# #   def __get__(self, instance, owner_class):
# #     if instance is None:
# #       return self
# #     return instance.__dict__.get(self.property_name)
# #
# # class Person:
# #   name = ValidString()
# #
# #   def __init__(self, name):
# #     self.name = name
# #
# #
# # p1 = Person("James")
# # p2 = Person("Bob")
# #
# # class Meta(type):
# #     def __new__(mcs, name, bases, dct):
# #         @classmethod
# #         def foo(cls):
# #             return 'Hello from classmethod: '
# #         dct['myfoo'] = foo
# #         return super().__new__(mcs, name, bases, dct)
# #
# #
# # class MyClass(metaclass=Meta):
# #     pass
# #
# # print(MyClass.myfoo())
#
# #
# #
# # class Lambda:
# #     def __init__(self, labdass: str):
# #         self.labda = eval(labdass)
# #
# #     def __call__(self, *args, **kwargs):
# #         return self.labda(*args, **kwargs)
# #
# # ob = Lambda('lambda x, y: x + y')
# # print(ob(122, 27))
# #
# #
# #
# #
#
#
#
#
#
#
#
#
#
#
# #
# #
# #
# #
# #
# #
# # def create_class(name, bases, attrs, methods):
# #     class_dict = {}
# #     for attr_name, attr_value in attrs.items():
# #         class_dict[attr_name] = attr_value
# #     for method_name, method_body in methods.items():
# #         exec(f'def {method_name}(self, *args, **kwargs):\n' + '\n'.join(f'    {line}' for line in method_body.split('\n')), globals(), class_dict)
# #         # print(' '.join(f'    {line}' for line in method_body.split('\n')), globals(), class_dict)
# #     # print(class_dict)
# #     return type(name, bases, class_dict)
# #
# #
# # attrs = {
# #     'attribute1': 'value1',
# #     'attribute2': 42,
# # }
# # methods = {
# #     'method1': """
# # print("Hello from method1")
# # """,
# #     'method2': """
# # print("attribute1 is", self.attribute1)
# # print("attribute2 is", self.attribute2)
# # """,
# # }
# #
# # MyDynamicClass = create_class('MyDynamicClass', (), attrs, methods)
# #
# #
# # instance = MyDynamicClass()
# #
# # print(instance.attribute1)
# # print(instance.attribute2)
# #
# # instance.method1()
# # instance.method2()
#
#
#
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
#
# class Dog:
#     def sound(self):
#         return "Woof!"
#
# # Registering Dog as a virtual subclass of Animal
# Animal.register(Dog)
#
# # Example usage
# def make_sound(animal):
#     return animal.sound()
#
# dog = Dog()
# print(make_sound(dog))
# print(isinstance(dog,Animal))
#
#
# #
# def typechecher(cls):
#     def wrapper(*args,**kwargs):
#         if not  isinstance(args[0],str) or not  isinstance(args[1],int):
#             raise TypeError("invalid type")
#         return cls(*args, **kwargs)
#     return wrapper
# @typechecher
# class Myclass:
#     name:str
#     age:int
#
#     def __init__(self,name,age):
#         self.age  = age
#         self.name = name
#
# cl = Myclass("john",21)
# import weakref
#
# class Stringvalue:
#     def __init__(self):
#         self.value = weakref.WeakKeyDictionary
#
#     def __get__(self,instance,owner):
#         if instance is None:
#             return self
#         return instance.__dict__.get(instance,None)
#
#     def __set__(self, instance, value):
#         if not isinstance(value,str):
#             raise ValueError("dfgvbn")
#         instance.__dict__[instance] = value
#
#
# class Myclass:
#     name = Stringvalue()
#
#     def __init__(self,name):
#         self.name = name
#
#
# cl = Myclass("Alik")
# cl.name="vzgo"
# print(cl.name)


# class Vector:
#     def __init__(self,*args):
#         self.data  = list(args)
#
#     def __bool__(self):
#         return any(self.data)
#     def __len__(self):
#         return len(self.data)
#     def __eq__(self, other):
#         if not isinstance(other,Vector):
#             return False
#         return self.data == other.data
#
#     def __add__(self, other):
#         if not isinstance(other,Vector):
#             raise TypeError("dfgbhn")
#         if len(self) != len(other):
#             raise ValueError("zxdfghj")
#         Vector(x+y for x,y in zip(self.data,other.data))
#
#
#     def __iadd__(self, other):
#         if not isinstance(other,Vector):
#             raise TypeError("dfgbhn")
#         if len(self) != len(other):
#             raise ValueError("zxdfghj")
#         self.data = [x+y for x,y in zip(self.data,other.data)]
#         return self.data
#
#     def __radd__(self, other):
#         if  isinstance(other,(int,float)):
#             return Vector(*(other+x for x in self.data))
#         else:
#             raise TypeError("hgcffh")
#
#     def __str__(self):
#         return f"our data is {self.data}"
#
# v1 = Vector(1,2,3)
# scalar = 5
# result = scalar + v1
# print(result)


# final

# class FinalInh(type):
#     def __new__(mcls,name,bases,cls_dict):
#         for base in bases:
#             if isinstance(base,FinalInh):
#                 raise TypeError(f"You cannot inherit from class {base.__name__}")
#         return super().__new__(mcls,name,bases,cls_dict)
#
#
# class A(metaclass=FinalInh):
#     pass
#
# class B(A):
#     pass


# class FinalOvr(type):
#     def __new__(mcls, name,bases,cls_dict):
#         for base in bases:
#             for attr in cls_dict.keys():
#                 if (
#                     not attr in ('__module__','__qualname__','__weakref__','__doc__') and
#                     attr in base.__dict__.keys()
#
#                 ):
#                     raise TypeError("sdfghbn")
#         return super().__new__(mcls,name,bases,cls_dict)
#
#
# class A(metaclass=FinalOvr):
#     def foo(self):
#         pass
#
# class B(A):
#
#     def foo(self):
#         pass


# def partial(func,*args,**kwargs):
#     def inner_func(*more_args,**more_kwargs):
#         all_args = more_args+args
#         all_kwargs = {**kwargs,**more_kwargs}
#         return func(*all_args,**all_kwargs)
#     return inner_func
#
# def add(a,b,c):
#     return a+b+c
#
# add_partial = partial(add,2,3)
# print(add_partial(4))

















































