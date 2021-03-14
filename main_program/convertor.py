class Convertor:
    """
    Conversion of a tree to a char chain
    """
    def get_all_char_compress(root):
        """
        Return the list of each char and converted value

        Attrs:
            root (Node): root of the tree that we want to convert

        returns:
            list: contains sub-lists of char and converted value
        """
        list_path = []
        list_leaf = root.get_all_leaf()
        list_node = root.get_all_node()

        for l in list_leaf:
            code = ""
            path = root.get_path(l)
            for n in path:
                if(n != root):
                    code += n.get_value()
            list_path.append([l.get_label(), code])
        
        return list_path


    def get_text_compress(root, text):
        """
        Return the converted text related to the text passed as a parameter

        Attrs:
            root (Node): root of the tree that we want to convert
            text (str): text we want to convert (related to the root passed as a parameter)

        Returns:
            str: converted/compressed text
        """
        list_char_compress = Convertor.get_all_char_compress(root)
        compressed_text_str = ""
        
        for c in text:
            for cc in list_char_compress:
                if(c == cc[0]):
                    compressed_text_str += cc[1]
        
        #compressed_text_str_oct = Convertor.transform_to_octet(compressed_text_str)
        
        #return compressed_text_str_oct
        return compressed_text_str


    def transform_to_octet(text):
        """
        Transform a binary string to a octet string

        Attrs:
            text (str): string with binary values

        Returns:
            str: tring with octet values
        """
        cpt = 0
        text_octet = ""
        text_tempo = ""
        for c in text:
            cpt += 1
            text_tempo += c
            if(cpt >= 8):
                text_octet += str(bytes([int(bin(int(text_tempo, 2)), 2)]))
                cpt = 0
                text_tempo = ""

        return text_octet

    def compression_ratio(text_to_compress, text_compressed):
        """
        Return the ratio of compression

        Attrs:
            text_to_compress (str): initial text not converted
            text_compressed (str): text already compressed

        Returns:
            float: ratio of compression
        """
        return 1 - (len(text_compressed) / (len(text_to_compress) * 8))

    def get_average_storage_bits(root):
    	"""
    	Return the average storage bits of a compressed character

    	Attrs:
    	    root (Node): root of the tree that we want to convert

    	Returns:
    		float: average storage bits of a compressed character
    	"""
        list_char_compress = Convertor.get_all_char_compress(root)

        res = 0
        for l in list_char_compress:
        	res += len(l[1])

        res = res/len(list_char_compress)

        return res



            