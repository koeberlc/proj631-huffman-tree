class Node:

	def __init__(self, label, frequence, left_child=None, right_child=None):
		self.label = label
		self.frequence = frequence
		self.left_child = left_child
		self.right_child = right_child
		self.value = None


	def get_left_child(self):
		return self.left_child

	def get_right_child(self):
		return self.right_child

	def get_label(self):
		return self.label

	def get_frequence(self):
		return self.frequence

	def get_value(self):
		return self.value

	def get_list_prefixe(self, node = "Error"):
		if(node == "Error"):
			node = self
		res = ""
		if(not node is None):
			res = node.get_label() + node.get_list_prefixe(node.get_left_child()) + node.get_list_prefixe(node.get_right_child())
		return res


	def is_leaf(self):
		return (self.get_right_child() is None) and (self.get_right_child() is None)


	def get_all_node(self):
		list_node = [self]
		if(not self.is_leaf()):
			if(not self.get_right_child() is None):
				list_node += self.get_right_child().get_all_node()
			list_node += self.get_left_child().get_all_node()
		return list_node

	def get_all_leaf(self):
		list_leaf = []
		list_node = self.get_all_node()
		for n in list_node:
			if(n.is_leaf()):
				list_leaf.append(n)
		return list_leaf

	def get_path(self,node):
		path = []
		list_node = self.get_all_node()

		while self!=node:
			for n in list_node:
				if(n.get_left_child() == node or n.get_right_child() == node):
					path.append(node)
					node = n

		path.append(self)
		path.reverse()

		return path