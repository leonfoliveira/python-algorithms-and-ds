class Heap:
	def __init__(self):
		self.heap = []
	
	def get_min(self):
		if len(self.heap) == 0:
			raise Exception('Empty heap')
		return self.heap[0]
	
	def insert(self, value):
		self.heap.append(value)
		self._heapfy_up(len(self.heap) - 1)
	
	def pop(self):
		if len(self.heap) == 0:
			raise Exception('Empty heap')
		self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
		temp = self.heap.pop()
		self._heapfy_down(0)
		return temp
		
	def _get_parent(self, index):
		return (index - 1) // 2		
	
	def _get_left_child(self, index):
		return 2 * index + 1
	
	def _get_right_child(self, index):
		return 2 * index + 2
	
	def _is_leaf(self, index):
		return self._get_left_child(index) >= len(self.heap)
	
	def _heapfy_up(self, index):
		if index == 0:
			return
		parent = self._get_parent(index)
		if self.heap[index] < self.heap[parent]:
			self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
			self._heapfy_up(parent)
	
	def _heapfy_down(self, index):
		left = self._get_left_child(index)
		right = self._get_right_child(index)
		
		if self._is_leaf(index):
			return
		
		left_val = self.heap[left] if left < len(self.heap) else float('inf')
		right_val = self.heap[right] if right < len(self.heap) else float('inf')
		
		if left_val <= right_val:
			self.heap[index], self.heap[left] = self.heap[left], self.heap[index]
			self._heapfy_down(left)
		else:
			self.heap[index], self.heap[right] = self.heap[right], self.heap[index]
			self._heapfy_down(right)
	
	def __str__(self):
		return f'[{", ".join(map(str, self.heap))}]'


from random import randint

heap = Heap()
print(heap)
for i in range(10):
	heap.insert(randint(0, 100))
print(heap)
print(heap.get_min())
for i in range(10):
	print(heap.pop())
print(heap)
