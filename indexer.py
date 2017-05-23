import nltk
import os
from bs4 import BeautifulSoup

for root, dirs, files in os.walk("./WEBPAGES_CLEAN"):
	for name in files:
		document = os.path.join(root,name)
		# print(document)
		file_content = open(document, encoding = 'utf-8').read()
		content = get_text(file_content)
		print(content)
			# tokens = nltk.word_tokenize(file_content)
			# print(tokens)
		# except:
		# 	pass