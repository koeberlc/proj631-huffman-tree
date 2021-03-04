class File:
	def __init__(self,path):
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
