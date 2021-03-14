from main_program.huffman import Huffman

# Compression initialization:
huffman_algo = Huffman()



# Compression
filename = "bonjour"

text_compressed, average_storage_bit, list_char_freq, ratio = huffman_algo.compress(filename)
