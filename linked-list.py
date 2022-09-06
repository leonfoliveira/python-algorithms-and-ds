class LinkedList:
	class LinkedListNode:
		def __init__(self, value, prev = None, next = None):
			self.value = value
			self.prev = prev
			self.next = next
			
	
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0
	
	def append(self, value):
		node = self.LinkedListNode(value)
		if self.head == None:
			self.head = node
			self.tail = node
		else:
			node.prev = self.tail
			self.tail.next = node
			self.tail = node
		self.length += 1
	
	def appendLeft(self, value):
		node = self.LinkedListNode(value)
		if self.head == None:
			self.head = node
			self.tail = node
		else:
			node.next = self.head
			self.head.prev = node
			self.head = node
		self.length += 1
	
	def pop(self):
		if self.tail == None:
			return None
		node = self.tail
		self.tail = self.tail.prev		
		if self.tail != None:
			self.tail.next = None
		else:
			self.head = None
		self.length -= 1
		return node
	
	def popLeft(self):
		if self.head == None:
			return None
		node = self.head
		self.head = self.head.next
		if self.head != None:
			self.head.prev = None
		else:
			self.tail = None
		self.length -= 1
		return None
	
	def sort(self):
		self.head = self._merge_sort(self.head)
	
	def _merge_sort(self, head):		
		if head == None or head.next == None:
			return head
					
		mid = self._get_mid(head)
		right = mid.next
		mid.next = None
		
		result = self._merge(self._merge_sort(head), self._merge_sort(right))
		return result			
	
	def _get_mid(self, head):
		curr = head
		curr2 = head
		while curr2.next != None and curr2.next.next != None:
			curr = curr.next
			curr2 = curr2.next.next
		return curr		
	
	def _merge(self, head_1, head_2):
		head = self.LinkedListNode(None)
		curr = head
		while head_1 != None and head_2 != None:
			if head_1.value < head_2.value:
				curr.next = head_1
				head_1 = head_1.next
			else:
				curr.next = head_2
				head_2 = head_2.next
			curr = curr.next
		if head_1 != None:
			curr.next = head_1
		else:
			curr.next = head_2
		return head.next		
	
	def __str__(self):
		curr = self.head
		items = []
		while curr != None:
			items.append(str(curr.value))
			curr = curr.next
		return f'[{", ".join(items)}]'

l = LinkedList()
l.append(5)
l.append(6)
l.appendLeft(4)
l.appendLeft(3)
print(l)
print(l.length)
l.pop()
l.popLeft()
print(l)
print(l.length)
l.pop()
l.popLeft()
print(l)
print(l.length)

from random import randint

for i in range(10):
	l.append(randint(0, 100))
print(l)
l.sort()
print(l)
