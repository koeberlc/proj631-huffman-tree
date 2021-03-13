from main_program.constant import Constant
from main_program.file import File
from main_program.frequence import Frequence
from main_program.tree import Node
from main_program.convertor import Convertor

from operator import attrgetter

class Huffman:
    """
    Class Huffman that compress an initial text
    """
    def compress(self, filename):
        """
        Compression fonction

        Attrs:
            filename (str): name of the file that we want to compress

        Returns:
            str: compressed text
            float: ratio of compression
        """
        constant = Constant()

        path_to_compress = constant.getElement("to_text_to_convert")
        path_to_lexicon = constant.getElement("to_lexicon")
        path_to_compressed = constant.getElement("to_text_converted")

        file_to_compress = File(path_to_compress + filename + ".txt")
        file_lexicon = File(path_to_lexicon + filename + ".txt")
        file_compressed = File(path_to_compressed + filename + ".bin")

        text_to_compress = file_to_compress.read()

        liste_char_freq = Frequence.get_frequence(text_to_compress)
        
        file_lexicon.writeCharFreq(liste_char_freq)

        root = self.make_tree(liste_char_freq)

        text_converted = Convertor.get_text_compress(root, text_to_compress)
        ratio = Convertor.compression_ratio(text_to_compress,text_converted)

        file_compressed.write(text_converted)

        return text_converted, liste_char_freq, ratio

    
    def make_tree(self, list_tupple):
        """
        Create a tree based on a list of tupple (char, frequency)

        Attrs:
            list_tupple (tupple): tupple list of char, frequency

        Returns:
            Node: root of the created tree
        """
        list_node = []
        for t in list_tupple:
            list_node.append(Node(t[0], t[1]))


        while len(list_node) > 1:
            list_node.sort(key=attrgetter('frequence'))
            n1, n2 = list_node[0], list_node[1]
            current_node = Node(None, n1.get_frequence() + n2.get_frequence(), n1, n2) 

            list_node.pop(0)
            list_node.pop(0)
            list_node.append(current_node)

        root = list_node[0]

        self.set_values(root)

        return root

    def set_values(self, node):
        """
        Set a value of each node: 
            each left child is set to 0
            each right child is set to 1

        Attrs:
            node (Node): node that we want to set his children
        """
        l_child = node.get_left_child()
        r_child = node.get_right_child()

        if(l_child is not None):
            l_child.value = "0"
            self.set_values(l_child)
        if(r_child is not None):
            r_child.value = "1"
            self.set_values(r_child)

    
