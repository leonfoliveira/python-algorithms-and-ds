class Stack:
	class StackNode:
		def __init__(self, value, prev = None):
			self.value = value
			self.prev = prev

	def __init__(self):
		self.head = None
	
	def push(self, value):
		self.head = self.StackNode(value, self.head)
		
	def pop(self):
		if self.head == None:
			return None
		node = self.head
		self.head = self.head.prev
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
			curr = curr.prev
		if len(result) == 0:
			return '[]'
		return f'[{", ".join(map(str, reversed(result)))}]'


st = Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
print(st)
print(st.pop())
print(st)
print(st.peek())

