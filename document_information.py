class docinfo:
	def __init__(self, docID):
		self.docID = docID
		self.term_frequency = 0
		self.inverse_term_frequency = 0
		self.special = 0
		self.tfidf = 0

	def __str__(self):
		return str(self.docID) + " freq: " + str(self.term_frequency) + " special: " + str(self.special) + " tf-idf: " str(self.tfidf)
