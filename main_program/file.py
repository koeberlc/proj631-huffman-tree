class File:
	def __init__(self, path):
		self.path = path

	def read(self):
		f = open(self.path, "r")
		text = f.read()
		f.close()
		return text

	def write(self, text):
		f = open(self.path, "w")
		f.write(text)
		f.close()

	def writeCharFreq(self, list_char_freq):
		text = str(len(list_char_freq)) + "\n"
		for cf in list_char_freq:
			text += str(cf[0]) + " " + str(cf[1]) + "\n"

		self.write(text)