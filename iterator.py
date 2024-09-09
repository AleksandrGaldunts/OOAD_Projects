# Iterator design pattern

                       

class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __next__(self):
        if self.index < len(self.collection):
            item = self.collection[self.index]
            self.index += 1
            return item
        raise StopIteration


class Aggregate:
    def __init__(self, collection):
        self.collection = collection

    def __iter__(self):
        return Iterator(self.collection)


aggregate = Aggregate([1, 2, 3, 4])
for item in aggregate:
    print(item)

print(dir(Aggregate))


