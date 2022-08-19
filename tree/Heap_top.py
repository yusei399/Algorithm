import heapq
import numbers

numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heap_data = []

for num in numbers:
	heapq.heappush(heap_data, num)

print(heap_data)

while heap_data:
	print(heapq.heappop(heap_data))