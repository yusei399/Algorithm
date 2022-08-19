from itertools import count
from multiprocessing.sharedctypes import Value
from traceback import print_tb
from typing import Counter, List

def min_count_remove(x: List[int], y: List[int]) -> None:
	# count_x = {}
	# count_y = {}
	# for i in x:
	# 	count_x[i] = count_x.get(i, 0) + 1
	# for i in y:
	# 	count_y[i] = count_y.get(i, 0) + 1
	counter_x = Counter(x) 
	counter_y = Counter(y) 
	print(counter_x)
	print(counter_y)

	for key_x, value_x in counter_x.items():
		value_y = counter_y.get(key_x)
		if value_y:
			if value_x < value_y:
				x[:] = [i for i in x if i != key_x]
			elif value_y > value_y:
				y[:] = [i for i in y if i != key_x]

if __name__ == '__main__':
	x = [1, 2, 3, 4, 4, 5, 5, 8, 10]
	y = [4, 5, 5, 5, 6, 7, 8, 8, 9, 10]
	print('x = ', x)
	print('y = ', y)
	min_count_remove(x, y)
	print('x = ', x)
	print('y = ', y)