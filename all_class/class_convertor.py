class Convertor:
	def get_all_char_compress(root):
		list_path = []
		list_leaf = root.get_all_leaf()
		list_node = root.get_all_node()

		for l in list_leaf:
			code = ""
			path = root.get_path(l)
			for n in path:
				if(n!=root):
					code += n.get_value()
			list_path.append([l.get_label(),code])
		
		print(list_path)
		return list_path


	def get_text_compress(root, text):
		list_char_compress = Convertor.get_all_char_compress(root)
		compressed_text_str = ""
		
		for c in text:
			for cc in list_char_compress:
				if(c == cc[0]):
					compressed_text_str += cc[1]

		print(compressed_text_str)
		print(bin(int(compressed_text_str,2)))

		
		#compressed_text_str_oct = Convertor.transform_to_octet(compressed_text_str)
		
		#return compressed_text_str_oct
		return compressed_text_str


	def transform_to_octet(text):
		cpt = 0
		text_octet = ""
		text_tempo = ""
		for c in text:
			cpt+=1
			text_tempo+=c
			if(cpt >=8):
				print(text_tempo)
				text_octet += str(bytes([int(bin(int(text_tempo,2)),2)]))
				cpt = 0
				text_tempo = ""
		print(text_octet)
		return text_octet

	def compression_ratio(text_to_compress, text_compressed):
		return 1-(len(text_compressed)/(len(text_to_compress)*8))


			