from main_program.constant import Constant
from main_program.huffman import Huffman

# Initialisation :
constant = Constant()

constant.addElement("to_text_to_convert", "text/text_to_convert/")
constant.addElement("to_text_converted", "text/text_converted/")
constant.addElement("to_lexicon", "text/lexicon/")

huffman_algo = Huffman()



# Compression
file = "bonjour"

huffman_algo.compress(constant, file)


# all_class -> main_prog -> point commun (pour faire un dossier)
# dans readme -> expliquer les class/fichiers
			# -> notion SOLID ?

# Faire des Tests Unitaires (voir doc Unittest)
# Faire doc de présentation (Projet, class, UML ...)