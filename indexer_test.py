from nltk.tokenize import RegexpTokenizer
import os
from bs4 import BeautifulSoup
import document_information as di
import re
from collections import Counter

index = dict() #list of objects
strong_index = dict() #list of tuples
heading_index = dict() #list of tuples

for root, dirs, files in os.walk("./WEBPAGES_CLEAN"):

	for name in files:
	
		document = os.path.join(root,name)

		soup = BeautifulSoup(open(document, encoding = 'utf-8').read(), "html.parser")

		tokenizer = RegexpTokenizer(r'\w+')

		#BODY TAGS

		tokens = [] #all the tokens in the body

		for content in soup.find_all('body'):
			for term in tokenizer.tokenize(content.text):
				term = term.lower()
				tokens.append(term)

		counts = Counter(tokens)

		for k,v in counts.items():
			if k not in index:
				index[k] = set()
			new_docinfo = di.docinfo(document)
			new_docinfo.term_frequency = v
			new_docinfo.special = 0
			index[k].add(new_docinfo)

		# UNCOMMENT STRONG TAGS AND HEADING TAGS TO INDEX THOSE
		
		# #STRONG TAGS

		# tokens = []

		# for content in soup.find_all('strong'):
		# 	for term in tokenizer.tokenize(content.text):
		# 		term = term.lower()
		# 		tokens.append(term)

		# counts = Counter(tokens)

		# #create separate index
		# for k,v in counts.items():
		# 	if k not in strong_index:
		# 		strong_index[k] = set()
		# 	strong_index[k].add((document, v))

		# #HEADING TAGS

		# tokens = []

		# for content in soup.find_all(['h1', 'h2', 'h3']):
		# 	for term in tokenizer.tokenize(content.text):
		# 		term = term.lower()
		# 		tokens.append(term)

		# counts = Counter(tokens)

		# #create separate index
		# for k,v in counts.items():
		# 	if k not in heading_index:
		# 		heading_index[k] = set()
		# 	heading_index[k].add((document, v)) 





# TESTING/PRINTING STUFFS

	# for key,value in heading_index.items():
	# 	print(key + '\n')
	# 	print(value)
	# 	print('\n')

for keys,values in index.items():
    # print("keys " + str(keys))
    # for k in values:
    # 	print("value: " + str(k))
    # print('\n')

    if keys == "irvine":
    	print(keys)
    	print (len(values))




