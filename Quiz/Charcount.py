import operator
from typing import Counter, Tuple

def count_char_v1(strings: str) -> Tuple[str, int]:
	strings = strings.lower()
	l =[]
	# for char in strings:
	# 	if not char.isspace():
	# 		l.append((char, strings.count(char)))
	l = [[c, strings.count(c)] for c in strings if not c.isspace()]
	return max(l, key=operator.itemgetter(1))

def count_char_v2(strings: str) -> Tuple[str, int]:
	strings = strings.lower()
	d = {}
	for char in strings:
		if not char.isspace():
			d[char] = d.get(char, 0) + 1
	max_key = max(d, key=d.get)
	return max_key, d[max_key]

def count_char_v3(strings: str) -> Tuple[str, int]:
	strings = strings.lower()
	d = Counter()
	for char in strings:
		if not char.isspace():
			d[char] = d.get(char, 0) + 1
	max_key = max(d, key=d.get)
	return max_key, d[max_key]

if __name__ == '__main__':
	s = 'This is a pen. This is an apple Applepen'
	print(count_char_v1(s))