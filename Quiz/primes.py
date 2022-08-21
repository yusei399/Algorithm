from typing import List

def generate_primes_v1(numbers: int) -> List[int]:
	primes = []
	for x in range(2, numbers + 1):
		for y in range(2, x):
			if x % y == 0:
				break
		else:
			primes.append(x)
	return primes

def generate_primes_v2(numbers: int) -> List[int]:
	primes = []
	cache = {}
	for x in range(2, numbers + 1):
		is_prime = cache.get(x)
		if is_prime is False:
			continue
		primes.append(x)
		cache[x] = True
		for y in range(x**2, numbers + 1, x):
			cache[y] = False
	return primes

if __name__ == '__main__':
	print(generate_primes_v1(50))
	print(generate_primes_v2(50))