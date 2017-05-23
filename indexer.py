from nltk.tokenize import RegexpTokenizer
import os
from bs4 import BeautifulSoup
import document_information as di

index = dict() #list of objects

for root, dirs, files in os.walk("./WEBPAGES_CLEAN_TEST"):
	for name in files:
		document = os.path.join(root,name)
		print("docid: " + document) #./WEBPAGES_CLEAN\0\102

		# file_content = open(document, encoding = 'utf-8').read()
		# print(file_content)
		# soup = BeautifulSoup(file_content, 'html.parser')

		soup = BeautifulSoup(open(document, encoding = 'utf-8').read(), "html.parser")

		tokenizer = RegexpTokenizer(r'\w+')
		tokenizer.tokenize('Eighty-seven miles to go, yet.  Onward!')

		for t in soup.find_all('body'):
			for w in tokenizer.tokenize(t.text):
				if w in index:
					index[w].term_frequency += 1
	
				elif w not in index:
					docinfo = di.docinfo(document)
					docinfo.term_frequency += 1
					index[w] = docinfo


					
	for keys,values in index.items():
	    print(keys)
	    print(values)


		# for t in soup.find_all('strong'):

			
		# print(soup.get_text())

		# print(content)

		# tokens = nltk.word_tokenize(file_content)
		# print(tokens)
		# # except:
		# # 	pass