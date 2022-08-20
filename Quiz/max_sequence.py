from operator import invert
from typing import List
from unittest import result

def get_max_sequence_sum(numbers: List[int]) -> int:
	result_sequence, sum_sequence = 0, 0
	for num in numbers:
		# temp_sum_sequence = sum_sequence + num
		# if num < temp_sum_sequence:
		# 	sum_sequence = temp_sum_sequence
		# else:
		# 	sum_sequence = num
		
		# if result_sequence < sum_sequence:
		# 	result_sequence = sum_sequence
		sum_sequence = max(num, sum_sequence + num)

		result_sequence = max(result_sequence, sum_sequence)
	return result_sequence

def find_max_circular_sequence_sum(numbers: List[int]) -> int:
	max_sequence_sum = get_max_sequence_sum(numbers)
	invert_numbers = []
	all_sum = 0
	for num in numbers:
		all_sum += num
		invert_numbers.append(-num)
	
	max_wrap_sequence = all_sum - (-get_max_sequence_sum(invert_numbers))
	return max(max_sequence_sum, max_wrap_sequence)

if __name__ == '__main__':
	print(find_max_circular_sequence_sum([1, -2, 3, 6, -1, 2, 4 -5, 2]))
