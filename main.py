from main_program.huffman import Huffman

# Initialization :
huffman_algo = Huffman()



# Compression
filename = "bonjour"

text_compressed, list_char_freq, ratio = huffman_algo.compress(filename)
