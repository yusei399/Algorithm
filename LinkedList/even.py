from __future__ import annotations
from cgi import print_environ
from hashlib import new
from typing import Any, OrderedDict

from nbformat import current_nbformat

class Node(object):
	def __init__(self, data: Any, next_node: Node = None):
		self.data = data
		self.next = next_node

class LinkedList(object):
	def __init__(self, head=None) -> None:
		self.head = head
	
	def append(self, data: Any) -> None:
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		
		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node
		
	def insert(self, data: Any) -> None:
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
	
	def print(self) ->None:
		current_node = self.head
		while current_node:
			print(current_node.data)
			current_node = current_node.next
	
	def remove(self, data: Any) -> None:
		current_node = self.head
		if current_node and current_node.data == data:
			self.head = current_node.next
			current_node = None
			return
		
		previous_node = None
		while current_node and current_node.data != data:
			previous_node = current_node
			current_node = current_node.next
		
		if current_node is None:
			return
		
		previous_node.next = current_node.next

	def reverse_iterative(self) -> None:
		previous_node = None
		current_node = self.head
		while current_node:
			next_node = current_node.next
			current_node.next = previous_node

			previous_node = current_node
			current_node = next_node
		
		self.head = previous_node
	
	def reverse_recurcive(self) -> None:
		def _reverse_recurcive(current_node:Node, previous_node: None):
			if not current_node:
				return previous_node
			next_node = current_node.next
			current_node.next = previous_node
			previous_node = current_node
			current_node = next_node
			return _reverse_recurcive(current_node, previous_node)
		self.head = _reverse_recurcive(self.head, None)
	
	def reverse_even(self) -> None:
		def _reverse_even(head: Node, previous_node: Node):
			if head is None:
				return None
			
			current_node = head
			while current_node and current_node.data % 2 == 0:
				next_node = current_node.next
				current_node.next = previous_node
				previous_node = current_node
				current_node = next_node
			if current_node != head:
				head.next = current_node
				_reverse_even(current_node, None)
				return previous_node
			else:
				head.next = _reverse_even(head.next, head)
				return head
		self.head = _reverse_even(self.head, None)


if __name__ == '__main__':
	l = LinkedList()
	l.append(2)
	l.append(4)
	l.append(6)
	l.append(1)
	l.print()
	print("######")
	l.reverse_iterative()
	l.reverse_even()
	l.print()