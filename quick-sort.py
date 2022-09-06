def quick_sort(array):
	def perform(left, right):
		if left >= right:
			return
		pivot = left
		end = right
				
		while left < right:
			while left < right and array[left] <= array[pivot]:
				left += 1
			while array[right] > array[pivot]:
				right -= 1
			if left < right:
				array[left], array[right] = array[right], array[left]
		array[right], array[pivot] = array[pivot], array[right]

		perform(pivot, right - 1)
		perform(right + 1, end)
		
	perform(0, len(array) - 1)
	return array


from random import randint

array = [randint(0, 100) for i in range(10)]
print(array)
print(quick_sort(array))
