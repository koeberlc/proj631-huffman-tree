class Constant:
    """
    Stock constants in a dict
    """
    def __init__(self):
        self.dict = {}

        self.addElement("to_text_to_convert", "text/text_to_convert/")
        self.addElement("to_text_converted", "text/text_converted/")
        self.addElement("to_lexicon", "text/lexicon/")

    def getDict(self):
        """
        Getter
        returns:
            dict: constant dictionary
        """
        return self.dict

    def addElement(self, key, value):
        """
        Add an element to the dictionary

        Attrs:
            key (str): name of the element
            value (str): value of the element
        """
        self.dict[key] = value

    def getElement(self, key):
        """
        Get the element related to a key

        Attrs:
            key (str): name of the element we want
        returns:
            str: element related to the key
        """
        return self.dict[key]
