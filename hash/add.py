
from functools import cache
from math import remainder
from traceback import print_tb
from typing import List, Tuple, Optional

def get_pair(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
		cache = set()
		for num in numbers:
			cache.add(num)
			val = target - num 
			if val in cache:
				return val, num

def get_pair_half_sum(numbers: List[int]) -> Optional[Tuple[int, int]]:
	sum_numbers = sum(numbers)
	half_sum, remainder = divmod(sum_numbers, 2)
	if remainder != 0:
		return

	if sum_numbers % 2 != 0:
		return
	half_sum = int(sum_numbers / 2)

	cache = set()
	for num in numbers:
		cache.add(num)
		val = half_sum - num 
		if val in cache:
			return val, num



if __name__ == '__main__':
	l = [11, 2, 5, 9, 10, 3]
	t = 12
	print(get_pair(l, t))
