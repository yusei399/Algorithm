from pickletools import read_uint1
from re import L
from typing import List, Tuple
from unittest import result

def fermat_last_theorem(max_num: int, squire_num: int) -> List[Tuple[int, int, int]]:
	result = []
	if squire_num < 2:
		return result

	max_z = int(pow((max_num - 1) ** 2 + max_num ** 2, 1.0 / squire_num))
	for x in range(1, max_num, + 1):
		for y in range(x + 1, max_num + 1):
			for z in range(y + 1, max_z):
				if pow(x, squire_num) + pow(y, squire_num) == pow(z, squire_num):
					result.append((x, y, z))
	return result

def fermat_last_theoremv2(max_num: int, squire_num: int) -> List[Tuple[int, int, int]]:
	result = []
	if squire_num < 2:
		return result

	max_z = int(pow((max_num - 1) ** 2 + max_num ** 2, 1.0 / squire_num))
	for x in range(1, max_num, + 1):
		for y in range(x + 1, max_num + 1):
			pow_sum = pow(x, squire_num) + pow(y, squire_num)
			z = pow(pow_sum, 1.0 / squire_num)
			z = int(z)
			z_pow = pow(z, squire_num)
			if z_pow == pow_sum:
				result.append((x, y, z))
	return result

if __name__ == '__main__':
	print('v1', fermat_last_theorem(10, 2))