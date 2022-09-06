# Returns the index of a target in an array
def binarySearch(array, target):
	left = 0
	right = len(array) - 1
	
	while left <= right:
		mid = (left + right) // 2
		# To avoid operating with large numbers use:
		# mid = left + (right - left) // 2
		if array[mid] == target:
			return mid
		elif array[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
		# More conditions can be added to find lower and upper bounds
				
	return -1
