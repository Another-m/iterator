class FlatIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.element_1 = 0
        self.element_2 = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.element_2 += 1
        if self.element_2 == len(self.nested_list[self.element_1]):
            self.element_1 += 1
            self.element_2 = 0
        if self.element_1 == len(self.nested_list):
            raise StopIteration
        return self.nested_list[self.element_1][self.element_2]


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

print(list(FlatIterator(nested_list)))