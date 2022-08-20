# s = 'racecar'
# print(s == ''.join(reversed(s)))
# print(s == s[::-1])



from typing import Tuple
from unittest import result


def is_paindrome(string: str) -> bool:
	len_string = len(string)
	if not len_string:
		return False
	if len_string == 1:
		return True
	
	start, end = 0, len_string - 1
	while start < end:
		if string[start] != string[end]:
			return False
		start += 1
		end -= 1
	return True

def find_paindrom(string: str, left: int, right: int):
	result = []
	while 0 <= left and right <= len(string) - 1:
		if string[left] != string[right]:
			break
		result.append(string[left:right + 1])
		left -= 1
		right += 1
	return result

def find_all_paindrom(string: str):
	result = []
	len_string = len(string)
	if not len_string:
		yield
	if len_string == 1:
		yield string
	
	for i in range(1, len_string - 1):
		yield from find_paindrom(string, i - 1, i + 1)
		yield from find_paindrom(string, i - 1, i)
	return result

if __name__ == '__main__':
	for s in find_all_paindrom('cabac'):
		print(s)