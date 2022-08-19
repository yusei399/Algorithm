from multiprocessing.sharedctypes import Value


class Node(object):
	def __init__(self, value: int) -> None:
		self.value = value
		self.left = None
		self.right = None

class BinarySearchTree(object):
	def __init__(self) -> None:
		self.root = None

	def insert(self, value: int) -> None:
		if self.root is None:
			self.root = None(value)
			return

		def _insert(node: Node, value: int) -> Node:
			if node is None:
				return Node(value)
			
			if value < node.value:
				node.left = _insert(node.left, value)
			else:
				node.right = _insert(node.right, value)
			return node
		_insert(self.root, value)
	
	def inorder(self) -> None:
		def _inorder(node :None) -> None:
			if node is not None:
				_inorder(node.left)
				print(node.value)
				_inorder(node.right)
		_inorder(self.root)

	def search(self, value:int) -> bool:
		def _search(node: Node, value: int) -> bool:
			if node is None:
				return False

			if node.value == value:
				return True
			elif node.value > value:
				return _search(node.left, value)
			elif node.value < value:
				return _search(node.right, value)
		return _search(self.root, value)

	def min_value(node: None) -> None:
		current = node
		while current.left is not None:
			current = current.left
		return current
	
	def remove(self, value:int) -> None:
		def _remove(node: Node, value: int) -> None:
			if node is None:
				return node
			if value < node.value:
				_remove(node.left, value)
			elif value > node.value:
				node.right = _remove(node.right, value)
			else:
				if node.left is None:
					return node.right
				elif node.right is None:
					return node.left
				
				temp = self.min_value(node.right)
				node.value = temp.value
				node.right = _remove(node.right, temp.value)
			return node
		_remove(self.root, value)



if __name__ == '__main__':
	root = None
	root = insert(root, 3)
	root = insert(root, 6)
	root = insert(root, 5)
	root = insert(root, 7)
	root = insert(root, 1)
	root = insert(root, 10)
	root = insert(root, 2)
	inorder(root)
	root = remove(root, 6)
	inorder(root)

	print(search(root, 1))
	print(search(root, 4))
	# print(root.value)
	# print(root.right.value)
