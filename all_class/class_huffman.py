from all_class.class_file import File

class Huffman:

	def compress(self, path):
		print(path)
		file_to_compress = File(path)
		text_to_compress = file_to_compress.read()
		print(text_to_compress)
		file_to_compress.write("test\ntest2")
		