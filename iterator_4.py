def flat_generator(nested_list):
	for i in nested_list:
		if type(i) == list:
			list_value = list(flat_generator(i))
			for value in list_value:
				yield value
		else:
			value = i
			yield value


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None]
]


for item in flat_generator(nested_list):
	print(item)

flat_list = [item for item in flat_generator(nested_list)]
print()
print(flat_list)
