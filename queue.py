class Queue:
	class QueueNode:
		def __init__(self, value, next = None):
			self.value = value		
			self.next = next

	def __init__(self):
		self.head = None
		self.tail = None
	
	def push(self, value):
		node = self.QueueNode(value)
		if self.tail == None:
			self.tail = node
			self.head = self.tail
		else:
			self.tail.next = node
			self.tail = node
		
	def pop(self):
		if self.head == None:
			return None
		node = self.head
		self.head = self.head.next
		if self.head == None:
			self.tail = None
		return node.value
		
	def peek(self):
		if self.head == None:
			return None
		return self.head.value
	
	def __str__(self):
		curr = self.head
		result = []
		while curr != None:
			result.append(curr.value)
			curr = curr.next
		if len(result) == 0:
			return '[]'
		return f'[{", ".join(map(str, result))}]'


qu = Queue()
qu.push(1)
qu.push(2)
qu.push(3)
qu.push(4)
qu.push(5)
print(qu)
print(qu.pop())
print(qu)
print(qu.peek())

