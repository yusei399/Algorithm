from gettext import ngettext
from readline import insert_text
from typing import List
from unittest import result


def snack_string_v1(chars: str) -> List[List[str]]:
	result = [[], [], []]
	result_indexes = {0, 1, 2}
	insert_index = 1
	for i, s in enumerate(chars):
		if i % 4 == 1:
			insert_index = 0
		elif i % 2 == 0:
			insert_index = 1
		elif i % 4 == 3:
			insert_index = 2
		result[insert_index].append(s)
		for rest_index in result_indexes - {insert_index}:
			result[rest_index].append(' ')
	return result

def snack_string_v2(chars: str, depth: int) -> List[List[str]]:
	result = [[] for _ in range(depth)]
	result_indexes = {i for i in range(depth)}
	insert_index = int(depth / 2)

	def pos(i):
		return i + 1
	
	def neg(i):
		return i - 1
	
	op = neg

	for s in chars:
		result[insert_index].append(s)
		for rest_index in result_indexes - {insert_index}:
			result[rest_index].append(' ')
		if insert_index <= 0:
			op = pos
		insert_index = op(insert_index)
	return result





if __name__ == '__main__':
	numbers = [str(i) for j in range(5) for i in range(10)]
	string = ''.join(numbers)
	for line in snack_string_v1(string):
		print(''.join(line))
	# print(snack_string_v1('01234'))

	import string
	alpha = [s for _ in range(2) for s in string.ascii_lowercase]
	strings = ''.join(alpha)
	for line in snack_string_v2(strings, 6):
		print(''.join(line))



