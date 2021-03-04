class Frequence:

	def get_frequence(text):
		#Create a array like [[characters],[frequences]]
		lex = [[],[]]

		for c in text:
			if not c in lex[0]:
				lex[0].append(c)
				lex[1].append(1)

			else:
				index = lex[0].index(c)
				lex[1][index]+=1

		#Create a new array like [[char1,freq1],[char2,freq2]]
		newLex = []
		for i in range(len(lex[0])):
			newLex.append((lex[0][i],lex[1][i]))
		
		#Sort the array by frequency then by character
		newLex.sort(key=itemgetter(1,0))

		return newLex