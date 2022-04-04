class FlatIterator:

    def __init__(self, data_list):
        self.data_list = data_list
        self.element_1 = -1
        self.element_2 = -1
        self.new_list = []
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.element_2 < len(self.data_list) - 1:
            if type(self.data_list[self.element_2 + 1]) == list:
                self.new_list = list(FlatIterator(self.data_list[self.element_2 + 1]))
                self.element_1 += 1
                if self.element_1 < len(self.new_list) - 1:
                    self.value = self.new_list[self.element_1]
                else:
                    self.value = self.new_list[self.element_1]
                    self.element_2 += 1
                    self.element_1 = -1
            else:
                self.element_2 += 1
                self.value = self.data_list[self.element_2]
        else:
            raise StopIteration

        return self.value


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
]


for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print()
print(flat_list)