class Constant:
	def __init__(self):
		self.dict = {}

	def getDict(self):
		return self.dict

	def addElement(self, key, value):
		self.dict[key] = value

	def getElement(self, key):
		return self.dict[key]
