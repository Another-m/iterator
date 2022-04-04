def flat_generator(nested_list):
    nested_list = [y for i in nested_list for y in i]
    return nested_list

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]


for item in  flat_generator(nested_list):
	print(item)

