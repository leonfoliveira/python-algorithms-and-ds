from collections import deque

class BinarySearchTree:
	class BinaryTreeNode:
		def __init__(self, value, left = None, right = None):
			self.value = value
			self.left = left
			self.right = right

	def __init__(self):
		self.root = None
	
	def insert(self, value):	
		node = self.BinaryTreeNode(value)
		self.root = self._insert(self.root, node)
		
	def search(self, value):
		return self._search(self.root, value)
	
	def remove(self, value):
		self.root = self._remove(self.root, value)
	
	def _insert(self, curr, node):
		if curr == None:
			return node
		if node.value < curr.value:
			curr.left = self._insert(curr.left, node)
		else:
			curr.right = self._insert(curr.right, node)
		return curr
	
	def _search(self, curr, value):
		if curr == None:
			return False
		if curr.value == value:
			return True
		if value < curr.value:
			return self._search(curr.left, value)
		return self._search(curr.right, value)
		
	def _remove(self, curr, value):
		if curr == None:
			return None
		if value < curr.value:
			curr.left = self._remove(curr.left, value)
		elif value > curr.value:
			curr.right = self._remove(curr.right, value)
		else:
			if curr.left == None:
				return curr.right
			if curr.right == None:
				return curr.left
			min_node = self._get_min_node(curr.right)
			self._remove(curr.right, min_node.value)
			curr.value = min_node.value
		return curr
	
	def _get_min_node(self, curr):
		if curr.left == None:
			return curr
		return self._get_min_node(curr.left)
			
	
	def __str__(self):
		queue = deque()
		queue.append(self.root)
		result = []
		while len(queue) > 0:
			node = queue.popleft()
			if node == None:
				result.append('#')
			else:
				result.append(str(node.value))
				queue.append(node.left)
				queue.append(node.right)
		return f'[{", ".join(result)}]'
			
	
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)
print(bst)
print(bst.search(4))
bst.remove(5)
print(bst)
bst.remove(4)
print(bst)
print(bst.search(4))
