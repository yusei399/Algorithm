from operator import imod
from typing import List

def comb_sort(numbers: List[int]) -> List[int]:
	len_numbers = len(numbers)
	gap = len_numbers
	swappd = True

	while gap != 1 or swappd:
		gap = int(gap / 1.3)
		if gap < 1:
			gap = 1

		swappd = False

		for i in range(0, len_numbers - gap):
			if numbers[i] > numbers[i + gap]:
				numbers[i], numbers[i + gap] = numbers[i + gap], numbers[i]

	return numbers

if __name__ == '__main__':
	import random
	nums = [random.randint(0, 1000) for _ in range(10)]
	print(comb_sort(nums))