import all_class.class_constant as const
import all_class.class_huffman as huffman

#Initialisation :
constant = const.Constant()
constant.addElement("to_text_to_convert","text/text_to_convert/")
constant.addElement("to_text_converted","text/text_converted/")
constant.addElement("to_lexicon","text/lexicon/")

huffman_tree = huffman.Huffman()