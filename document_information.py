class docinfo:
	def __init__(self, docID):
		self.docID = docID
		self.term_frequency = 0
		self.weight = None
	def __str__(self):
		return str(self.docID) + " " + str(self.term_frequency) + " " + str(self.weight)
