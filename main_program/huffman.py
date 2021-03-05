from main_program.file import File
from main_program.frequence import Frequence
from main_program.tree import Node
from main_program.convertor import Convertor
from main_program.constant import Constant

from operator import attrgetter

class Huffman:

	def compress(self, filename):

		# Initialisation Constant :
		constant = Constant()

		constant.addElement("to_text_to_convert", "text/text_to_convert/")
		constant.addElement("to_text_converted", "text/text_converted/")
		constant.addElement("to_lexicon", "text/lexicon/")

		path_to_compress = constant.getElement("to_text_to_convert")
		path_to_lexicon = constant.getElement("to_lexicon")
		path_to_compressed = constant.getElement("to_text_converted")

		file_to_compress = File(path_to_compress + filename + ".txt")
		file_lexicon = File(path_to_lexicon + filename + ".txt")
		file_compressed = File(path_to_compressed + filename + ".bin")

		text_to_compress = file_to_compress.read()

		liste_char_freq = Frequence.get_frequence(text_to_compress)
		
		file_lexicon.writeCharFreq(liste_char_freq)

		root = self.make_tree(liste_char_freq)

		text_converted = Convertor.get_text_compress(root, text_to_compress)
		ratio = Convertor.compression_ratio(text_to_compress,text_converted)

		file_compressed.write(text_converted)

		# Tests

		#print(path)
		#print(text_to_compress)
		#print(liste_char_freq)
		#print(root)
		print(ratio)
	
	def make_tree(self, list_tupple):
		list_node = []
		for t in list_tupple:
			list_node.append(Node(t[0], t[1]))


		while len(list_node)>1:
			list_node.sort(key=attrgetter('frequence'))
			n1, n2 = list_node[0], list_node[1]
			current_node = Node(n1.get_label() + n2.get_label(), n1.get_frequence() + n2.get_frequence(), n1, n2) 

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

	
