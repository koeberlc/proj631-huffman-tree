from main_program.huffman import Huffman

# Compression initialization:
huffman_algo = Huffman()



# Compression
filename = input("Select your file name (default: bonjour):")

if(filename == ""):
	filename = "bonjour"

text_compressed, average_storage_bit, list_char_freq, ratio = huffman_algo.compress(filename)

def displayOption():
	answer = ["1", "2", "3", "4", "5"]
	print("-------------------")
	print("Select an option:")
	print("1/ Display text compressed")
	print("2/ Display tupple character/frequency")
	print("3/ Display average storage bits of a compressed character")
	print("4/ Diplay compression ratio")
	print("5/ Quit")
	select = input()

	if(not select in answer):
		print("-------------------")
		print("Input error")
		

	if(select == "1"):
		print("Compressed text : \n" + str(text_compressed))
	if(select == "2"):
		print("Tupple character/frequency : \n" + str(list_char_freq))
	if(select == "3"):
		print("Average storage bits : \n" + str(average_storage_bit))
	if(select == "4"):
		print("Compression ratio : \n" + str(ratio))

	if(select != "5"):
		displayOption()


displayOption()

