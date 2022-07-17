from typing import List
from numpy import number

from torch import numel

def gnome_sort(numbers: List[int]) -> List[int]:
	len_numbes = len(numbers)
	index = 0
	while index < len_numbes:
		if index == 0:
			index = index + 1
		if numbers[index] >= numbers[index -1]:
			index += 1
		else:
			numbers[index], numbers[index -1] = numbers[index -1], numbers[index]
			index -=  1
	
	return numbers

if __name__ == '__main__':
	import random
	nums = [random.randint(0, 1000) for _ in range(10)]
	print(gnome_sort(nums))