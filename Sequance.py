class MySequance:
    def __init__(self, data=[]):
        self.data = data
    def __len__(self):
        return len(self.data)
    def __getitem__(self, item):
        return self.data[item]
    def __setitem__(self, key, value):
        self.data[key] = value

    def __repr__(self):
        return f"My list {self.data}"

l = MySequance([1,2,3])
l[1] = 10
print(l)
print(len(l))

