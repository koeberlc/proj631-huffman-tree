class File:
    """
    Class to read / write files
    """
    def __init__(self, path):
        self.path = path

    def read(self):
        """
        Read the file

        Returns:
            str: text from the file
        """
        f = open(self.path, "r")
        text = f.read()
        f.close()
        return text

    def write(self, text):
        """
        Write into the file

        Attrs:
            text (str): text we want to write
        """
        f = open(self.path, "w")
        f.write(text)
        f.close()

    def writeCharFreq(self, list_char_freq):
        """
        Transform the text with character and frequency list before writing it to the file

        Attrs:
            list_char_freq (str): character and frequency list
        """
        text = str(len(list_char_freq)) + "\n"
        for cf in list_char_freq:
            text += str(cf[0]) + " " + str(cf[1]) + "\n"

        self.write(text)