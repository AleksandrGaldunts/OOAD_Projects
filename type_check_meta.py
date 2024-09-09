class TypeCheckMeta(type):
    def __new__(cls, name, bases, dct):
        new_cls = super().__new__(cls, name, bases, dct)
        for attr_name, attr_value in dct.items():
            if callable(attr_value) and hasattr(attr_value, '__annotations__'):
                setattr(new_cls, attr_name, cls.wrap_method(attr_value))
        return new_cls

    @staticmethod
    def wrap_method(method):
        annotations = method.__annotations__
        def wrapper(*args, **kwargs):
            method_args = method.__code__.co_varnames[:method.__code__.co_argcount]
            for arg_name, arg_type in annotations.items():
                if arg_name in kwargs and not isinstance(kwargs[arg_name], arg_type):
                    raise TypeError(f"Argument '{arg_name}' must be of type {arg_type.__name__}")
                if arg_name in method_args:
                    arg_index = method_args.index(arg_name)
                    if arg_index < len(args) and not isinstance(args[arg_index], arg_type):
                        raise TypeError(f"Argument '{arg_name}' must be of type {arg_type.__name__}")
            return method(*args, **kwargs)

        return wrapper


# Example usage
class MyClass(metaclass=TypeCheckMeta):
    def foo(self, text: str, number: int) -> None:
        print(f"text = {text}, number = {number}")


obj = MyClass()

obj.foo("Hello", 123)
#
# try:
#     obj.foo("Hello", "world")
# except TypeError as e:
#     print(e)
