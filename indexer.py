from nltk.tokenize import RegexpTokenizer
import os
from bs4 import BeautifulSoup
import document_information as di
import re

#problems
#when looking for body tag, it counts the words in other tags, so it overcounts
#right now, i wrote the code assuming order (which is wrong)
#  so basically now it finds <strong> tags, counts it, deletes whatever is inside
#  and continues on to body
#  but does not account for <strong><h1> </h1></strong> and various orders
#also, broken tags and unfinished tags: ie, </strong>


index = dict() #list of objects

for root, dirs, files in os.walk("./WEBPAGES_CLEAN_TEST"):
	for name in files:
		document = os.path.join(root,name)
		# print("docid: " + document) #./WEBPAGES_CLEAN\0\102

		file_content = open(document, encoding = 'utf-8').read()

		fixed_content = re.sub(">\s*(\!--|\!DOCTYPE|\
                       a|abbr|acronym|address|applet|area|\
                       b|base|basefont|bdo|big|blockquote|body|br|button|\
                       caption|center|cite|code|col|colgroup|\
                       dd|del|dfn|dir|div|dl|dt|\
                       em|\
                       fieldset|font|form|frame|frameset|\
                       head|h1|h2|h3|h4|h5|h6|hr|html|\
                       i|iframe|img|input|ins|\
                       kbd|\
                       label|legend|li|link|\
                       map|menu|meta|\
                       noframes|noscript|\
                       object|ol|optgroup|option|\
                       p|param|pre|\
                       q|\
                       s|samp|script|select|small|span|strike|strong|style|sub|sup|\
                       table|tbody|td|textarea|tfoot|th|thead|title|tr|tt|\
                       u|ul|\
                       var)>", "><\g<1>>", file_content)

		# soup = BeautifulSoup(open(document, encoding = 'utf-8').read(), "html.parser")
		soup = BeautifulSoup(fixed_content, "html.parser")

		tokenizer = RegexpTokenizer(r'\w+')

		for t in soup.find_all('strong'):
			for w in tokenizer.tokenize(t.text):
				# print(w)
				if w in index: #term is already in index
					found = False
					for doc in index[w]:
						if doc.docID == document: #if we find a class object for this docid in the term set
							found = True
							doc.term_frequency += 1
							doc.special += 2
							break
					if not found:
						docinfo = di.docinfo(document)
						docinfo.term_frequency += 1
						docinfo.special += 2
	
				elif w not in index: #term is not in index
					index[w] = set()
					docinfo = di.docinfo(document)
					docinfo.term_frequency += 1
					docinfo.special += 2
					index[w].add(docinfo)
			t.extract()


		for t in soup.find_all('body'):
			for w in tokenizer.tokenize(t.text):
				# print(w)
				if w in index: #term is already in index
					found = False
					for doc in index[w]:
						if doc.docID == document: #if we find a class object for this docid in the term set
							found = True
							doc.term_frequency += 1
							doc.special += 1
							break
					if not found:
						docinfo = di.docinfo(document)
						docinfo.term_frequency += 1
						docinfo.special += 1


	
				elif w not in index: #term is not in index
					index[w] = set()
					docinfo = di.docinfo(document)
					docinfo.term_frequency += 1
					docinfo.special += 1
					index[w].add(docinfo)







	# 	for t in soup.find_all('strong'):
	# 		for w in tokenizer.tokenize(t.text):
	# 			if w in index: #term is already in index
	# 				for doc in index[w]:
	# 					if doc.docID == document: #if we find a class object for this docid in the term set
	# 						doc.term_frequency += 1
	# 						doc.weight += 2
	# 						break
	# 				docinfo = di.docinfo(document)
	# 				docinfo.term_frequency += 1
	# 				docinfo.weight += 2
 # 					# ADD INTO THE SET

	
	# 			elif w not in index: #term is not in index
	# 				index[w] = set()
	# 				docinfo = di.docinfo(document)
	# 				docinfo.term_frequency += 1
	# 				docinfo.weight += 2
	# 				index[w].add(docinfo)


	

	for keys,values in index.items():
	    # print("keys " + str(keys))
	    # for k in values:
	    # 	print("value: " + str(k))
	    # print('\n')
	    if keys == "hello":
	    	for i in values:
	    		print(i)








		# for t in soup.find_all('strong'):

			
		# print(soup.get_text())

		# print(content)

		# tokens = nltk.word_tokenize(file_content)
		# print(tokens)
		# # except:
		# # 	pass