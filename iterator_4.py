def flat_generator(nested_list):
	new_list = []
	for i in nested_list:
		if type(i) == list:
			value = flat_generator(i)
			new_list += value
		else:
			value = i
			new_list += [value]
	return new_list

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None]
]


for item in  flat_generator(nested_list):
	print(item)

flat_list = [item for item in flat_generator(nested_list)]
print()
print(flat_list)
