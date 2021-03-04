from all_class.class_file import File
from all_class.class_frequence import Frequence

class Huffman:

	def compress(self, path):
		
		file_to_compress = File(path)
		text_to_compress = file_to_compress.read()

		liste_char_freq = Frequence.get_frequence(text_to_compress)
		
		root = self.make_tree(liste_char_freq)


		#Tests
		print(path)
		print(text_to_compress)
		print(liste_char_freq)
		print(root)
	
	def make_tree(self, list_tupple):
		list_node = []
		for t in list_tupple:
			list_node.append(Node(t[0],t[1]))


		while len(list_node)>1:
			list_node.sort(key=attrgetter('frequence', 'label'), reverse=True)
			n1,n2 = list_node[0],list_node[1]
			current_node = Node(n1.get_label()+n2.get_label(), n1.get_frequence() + n2.get_frequence(),n1,n2) 

			list_node.pop(0)
			list_node.pop(0)
			list_node.append(current_node)

		root = list_node[0]

		self.set_values(root)

		return root

	def set_values(self, node):
		l_child = node.get_left_child()
		r_child = node.get_right_child()

		if(l_child is not None):
			l_child.value = "0"
			self.set_values(l_child)
		if(r_child is not None):
			r_child.value = "1"
			self.set_values(r_child)

