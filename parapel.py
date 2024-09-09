# # import weakref
# # class StringValue:
# #     # def __init__(self):
# #     #     self.value = weakref.WeakKeyDictionary()
# #     def __set_name__(self, owner, name):
# #         self.name = name
# #     def __get__(self, instance, owner):
# #         if instance is None:
# #             return self
# #         return instance.__dict__[self.name]
# #     def __set__(self, instance, value):
# #         if len(value)<8 or not isinstance(value,str):
# #             raise ValueError("vates ape")
# #         instance.__dict__[self.name]=value
# #
# #
# # class Person:
# #     surname = StringValue()
# #     password = StringValue()
# #
# #     def __init__(self,surname,password):
# #         self.surname = surname
# #         self.password = password
# #
# #
# #    # def getname(self):
# #    #      return self.__name
# #    #
# #    #
# #    #  def setname(self,value):
# #    #      self.__name = value
# #    #
# #    #  name = property(getname,setname)
# #    #
# #    #
# #    #  @property
# #    #  def age(self) -> int:
# #    #      return self. __name
# #    #
# #    #  @age.setter
# #    #  def age(self, value) -> None:
# #    #      self.__name = value
# #
# # p = Person("Hayrapetyan", "begemdwdwo")
# # print(p.__dict__)
# #
# #
# #
# # class Person:
# #     __slots__ = ('__name', '__age')
# #     def __init__(self,name,age):
# #         self.__age = age
# #         self.__name = name
# #
# #
# # p = Person("Alik", 21)
# #
# # print(p.__slots__)
# # print(dir(p))
# # # print(p.__dict__)
# # print(p._Person__age)
# # print(p._Person__name)
#
# # operator overloading
# class Person:
#     def __init__(self,age):
#         self.age = age
#
#     def __add__(self,other):
#         return Person(self.age + other.age)
#
#     def __radd__(self, other):
#         if isinstance(other, int) or isinstance(other, float):
#             return other + self.age
#         else:
#             raise TypeError("Unsupported operand type for +")
#
#     def __iadd__(self, other):
#         if isinstance(other,int) or isinstance(other,float):
#             self.age += other
#             return self
#         else:
#             raise TypeError("apeeeeeeeeeeeeeeee")
#
# p1 = Person(25)
# p2 = Person(26)
#
# p3 =p1+p2
# print(p3.age)
# print(20+p1)
# p1.age += "bulki"
# print(p1.age)
#
#
# class Person:
#     def __init__(self, value,ls):
#         self.ls = ls
#         self.value = value
#
#     def __eq__(self, other):
#         if isinstance(other,Person):
#             return self.value == other.value
#         return False
#     #
#     # def __len__(self):
#     #      return len(self.ls)
#
#     def __hash__(self):
#         return hash(self.value)
#
# p
#
#
#
# p2=Person(0, [])
# print(bool(p2))

# context manager implementation

# class FileContextManager:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
# # Using the context manager
# with FileContextManager('example.txt', 'w') as file:
#     file.write('Hello, world!')


# implement staticmethod and classmethod decorators

# class ClassMethod:
#     def __init__(self, method):
#         self.method = method
#
#     def __get__(self, instance, owner):
#         def new_method(*args, **kwargs):
#             return self.method(owner, *args, **kwargs)
#         return new_method
#
#
# class StaticMethod:
#     def __init__(self, method):
#         self.method = method
#
#     def __get__(self, instance, owner):
#         return self.method
#
#
# class MyClass:
#     @ClassMethod
#     def class_method(cls, x):
#         return "Class Method:", cls, x
#
#     @StaticMethod
#     def static_method(x):
#         return "Static Method:", x
#
#
# if __name__ == "__main__":
#     obj = MyClass()
#
#     # Calling class method
#     print(obj.class_method(10))  # Output: ('Class Method:', <class '__main__.MyClass'>, 10)
#
#     # Calling static method
#     print(obj.static_method(20))  # Output: ('Static Method:', 20)

#association through dependency injection

# class Engine:
#     @staticmethod
#     def start():
#         print("Engine started")
#
# class Car:
#     def __init__(self, engine):
#         self.engine = engine
#
#     def start(self):
#         self.engine.start()  # Association through dependency injection
#
# my_engine = Engine()
# my_car = Car(my_engine)
# my_car.start()  # Output: Engine started


# class Base:
#     def __init__(self):
#         print("Base initializer")
#     def foo(self):
#         return "foo() called"
# class DerivedA(Base):
#     def foo(self):
#         return "DerivedA foo() called"
# class DerivedB(Base):
#     def foo(self):
#         return "DerivedB foo() called"
# class DerivedC(DerivedA, DerivedB):
#     pass
# class DerivedD(DerivedB, DerivedA):
#     def foo(self):
#         return "DerivedD foo() called"
#
# # class E(DerivedC,DerivedD):   # error kta arden vorovhetev mro nery xachvecin
# #     pass
# objC = DerivedC()
# objD = DerivedD()
# print(objC.foo())
# print(objD.foo())


#############    __MRO__   ##################
# earlier than python 2.3


# class A:
#     pass
#
# class B(A):
#     pass
#
# class C(A):
#     pass
#
# class D(B, C):
#     pass
#
# class E(C):
#     pass
#
# class F(D, E):
#     pass
#
# # Printing MRO for each class
# print "MRO for A:", A.__bases__
# print "MRO for B:", B.__bases__
# print "MRO for C:", C.__bases__
# print "MRO for D:", D.__bases__
# print "MRO for E:", E.__bases__
# print "MRO for F:", F.__bases__


# vectori xndiry nmushi 9 rd harc

# class Vector:
#     def __init__(self, *args):
#         self._values = list(args)
#
#     def __bool__(self):
#         return any(self._values)
#
#     def __eq__(self, other):
#         return self._values == other._values
#
#     def __add__(self, other):
#         if len(self._values) != len(other._values):
#             raise ValueError("Vectors must be of same dimensions to perform addition.")
#         result_values = [x + y for x, y in zip(self._values, other._values)]
#         return Vector(*result_values)
#
#     def __iadd__(self, other):
#         if len(self._values) != len(other._values):
#             raise ValueError("Vectors must be of same dimensions to perform addition.")
#         self._values = [x + y for x, y in zip(self._values, other._values)]
#         return self
#
#     def __str__(self):
#         return "Vector(" + ", ".join(str(val) for val in self._values) + ")"
#
#     def __len__(self):
#         return len(self._values)
#
# # Example usage:
# v1 = Vector(1, 2, 3, 4, 5)
# v2 = Vector(1, 1, 1, 1, 1)
# print(bool(v1))  # Output: True
# print(bool(Vector(0, 0, 0)))  # Output: False
#
# v3 = v1 + v2
# print(v3)  # Output: Vector(2, 3, 4, 5, 6)
#
# v1 += v2
# print(v1)  # Output: Vector(2, 3, 4, 5, 6)
#
# print(len(v1))  # Output: 5
# print(len(Vector(1, 2)))  # Output: 2
#
# print(v1 == v3)  # Output: True

# class StaticMethod:
#     def __init__(self, func):
#         self.func = func
#
#     def __get__(self, instance, owner):
#         return self.func
#
# class MyClass:
#     @StaticMethod
#     def static_method():
#         print("This is a static method")
#
# x = MyClass()
# # Call the static method without creating an instance of MyClass
# MyClass.static_method()
# x.static_method()

class ClassMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        def method_with_class(*args, **kwargs):
            return self.func(owner, *args, **kwargs)
        return method_with_class

class MyClass:
    class_variable = "I am a class variable"

    @ClassMethod
    def class_method(cls):
        print("This is a class method")
        print("Accessing class variable:", cls.class_variable)

# Call the class method without creating an instance of MyClass
x = MyClass()
x.class_method()
MyClass.class_method()
























































