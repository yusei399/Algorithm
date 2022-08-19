from functools import cache
import time
from traceback import print_tb
# from functools import lru_cache

# @lru_cache()
def memoize(f):
	cache = {}
	def _wrapper(n):
		if not cache:
			cache[n] = f(n)
		return cache[n]
	return _wrapper

@memoize
def test(n):
	print('test')

def long_func(num: int) -> int:
	r = 0
	for i in range(10000000):
		r += num * i
	return r


if __name__ == '__main__':
	for i in range(10):
		print(long_func(i))
	
	start = time.time()
	for i in range(10):
		print(long_func(i))
	print(time.time() - start)
