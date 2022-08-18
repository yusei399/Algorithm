from __future__ import annotations
from hashlib import new
from logging import captureWarnings
from tkinter.messagebox import NO
from typing import Any, Optional

class Node(object):
	def __init__(self, data: Any, next_node: Node = None, prev_node : Node = None) -> None:
		self.data = data
		self.next = next_node
		self.prev = prev_node

class DoublyLinkedList(object):

	def __init__(self, head : Node=None) -> None:
		self.head = head
	
	def append(self, data:Any) -> None:
		new_node = Node(data)
		if self.head is None:
			self.head = new_node 
			return 
		
		current_node = self.head
		while current_node.next:
			current_node = current_node.next
		current_node.next = new_node
		new_node.prev = current_node
	
	def insert(self, data:Any) -> None:
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		
		self.head.prev = new_node
		new_node.next = self.head
		self.head = new_node

	
	def insert(self, data:Any)->None:
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return

	def print(self) -> None:
		current_node = self.head
		while current_node:
			print(current_node.data)
			current_node = current_node.next
	
	def remove(self, data:Any)-> None:
		current_node = self.head
		if current_node and current_node.data == data:
			if current_node.next is None:
				current_node = None
				self.head = None
				return
			else:
				next_node = current_node.next
				next_node.prev = None
				current_node = None
				self.head = next_node
				return
		
		while current_node and current_node.next != data:
			current_node = current_node.next
		
		if current_node is None:
			return




if __name__ == '__main__':
	d = DoublyLinkedList()
	d.append(1)
	d.append(2)
	d.append(3)
	print(d.head.data)
	print(d.head.next.data)
	print(d.head.next.next.prev.data)


