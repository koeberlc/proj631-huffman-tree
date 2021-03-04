from all_class.class_constant import Constant
from all_class.class_huffman import Huffman

#Initialisation :
constant = Constant()
constant.addElement("to_text_to_convert","text/text_to_convert/")
constant.addElement("to_text_converted","text/text_converted/")
constant.addElement("to_lexicon","text/lexicon/")

huffman_tree = Huffman()



#Compression
file = "bonjour"

path = constant.getElement("to_text_to_convert") + file + ".txt"

huffman_tree.compress(path)