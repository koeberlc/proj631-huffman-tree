from main_program.constant import Constant
from main_program.huffman import Huffman

# Initialization :
constant = Constant()

huffman_algo = Huffman()



# Compression
file = "bonjour"

text_compressed, list_char_freq, ratio = huffman_algo.compress(constant, file)


# all_class -> main_prog -> point commun (pour faire un dossier)
# dans readme -> expliquer les class/fichiers
            # -> notion SOLID ?

# Faire des Tests Unitaires (voir doc Unittest)
# Faire doc de présentation (Projet, class, UML ...)