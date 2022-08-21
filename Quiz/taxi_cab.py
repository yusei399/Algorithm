from collections import defaultdict
from typing import List, Tuple
from unittest import result

def taxi_cab_numeber(max_answer_num: int, match_answer_num: int = 2) -> List[Tuple[int, List[Tuple[int, int]]]]:
	result = []
	got_answer_count = 0
	answer = 1
	while got_answer_count < max_answer_num:
		match_answer_count = 0
		memo = defaultdict(list)

		max_param = pow(answer, 1.0 / 3)
		for x in range(1, 100):
			for y in range(x + 1, 100):
				if x ** 3 + y ** 3 == answer:
					match_answer_count += 1
					memo[answer].append((x, y))
		
		if match_answer_count == match_answer_num:
			result.append((answer, memo[answer]))
			got_answer_count += 1
		
		answer += 1
	return result


if __name__ == '__main__':
	print(taxi_cab_numeber(2, 2))