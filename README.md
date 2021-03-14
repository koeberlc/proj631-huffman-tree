# proj631-huffman-tree-code

Developpement project for the PROJ631 : project gestion.

In this project, I develop an Huffman algorithme that compress a text using its character frequency.


# How to use :
You only need to launch main.py using a python interpreter.

The program will ask you the file name containing the text that you want to compress.

Then a menu will show. By typing the right number and pressing enter you can :
* Display the compressed text
* Display the tupple character/frequency
* Diplay the average storage bits of a compressed character
* Diplay the compression ration


# Structure :
_main_program folder :_
All files related to the different classes

_text/lexicon folder :_
All the lexicon text files linked to a compressed text
Each file contains the number of different characters and each character linked to its frequency

_text/text_to_convert folder :_
All the text files we want to convert

_text/text_converted folder :_
All the bin files containing the compressed texts

# Tests :
You can find unit test in the _huffman_test.py_ file.
