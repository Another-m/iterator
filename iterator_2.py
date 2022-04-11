def flat_generator(nested_list):

	for value in nested_list:
		for item in value:
			yield item


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]


for item in  flat_generator(nested_list):
	print(item)

flat_list = [item for item in flat_generator(nested_list)]
print()
print(flat_list)
