def merge_sort(array):
	if len(array) < 2:
		return array
	
	mid = len(array) // 2
	left = merge_sort(array[:mid])
	right = merge_sort(array[mid:])
	
	result = []
	index_left = 0
	index_right = 0
	
	while index_left < len(left) and index_right < len(right):
		if left[index_left] < right[index_right]:
			result.append(left[index_left])
			index_left += 1
		else:
			result.append(right[index_right])
			index_right += 1
	
	if index_left < len(left):
		result += left[index_left:]
	if index_right < len(right):
		result += right[index_right:]
	
	return result


from random import randint

array = [randint(0, 100) for i in range(10)]
print(array)
print(merge_sort(array))
