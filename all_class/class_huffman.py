from all_class.class_file import File
from all_class.class_frequence import Frequence


class Huffman:

	def compress(self, path):
		
		file_to_compress = File(path)
		text_to_compress = file_to_compress.read()

		liste_char_freq = Frequence.get_frequence(text_to_compress)
		

		#Tests
		print(path)
		print(text_to_compress)
		print(liste_char_freq)
	


