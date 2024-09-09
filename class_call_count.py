# class Mlass:
#     def __init__(self):
#         self.index = 0
#     def __call__(self, *args, **kwargs):
#         self.index+=1
#         return self
#
#     def __str__(self):
#         return f"calls {self.index} times"
#
# x = Mlass()
# print(x()()())


class Mlass:
    def __init__(self):
        self.index = 0
    def __call__(self, *args, **kwargs):
        self.index+=1
        return self

     def __str__(self):
         return f"calls {self.index} times"

x = Mlass()
x()()()()()()()()

