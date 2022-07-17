from typing import List

from sort.Comb import comb_sort

def selection_sort(numbers:List[int]) -> List[int]:
	len_numbers = len(numbers)
	for i in range(len_numbers):
		min_index = i
		for j in range(i + 1, len_numbers):
			if numbers[min_index] > numbers[j]:
				min_index = j
		numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
	return numbers

if __name__ == '__main__':
	import random
	nums = [random.randint(0, 1000) for _ in range(10)]
	print(selection_sort(nums))