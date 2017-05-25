from nltk.tokenize import RegexpTokenizer
from codecs import encode, decode
import os
from bs4 import BeautifulSoup
import document_information as di
import re

'''
KNOWN ISSUES:

1) When looking for body tag, it counts the words in other tags, so it overcounts right now, 
    I wrote the code assuming order (which is wrong) so basically now it finds <strong> tags, 
    counts it, deletes whatever is inside and continues on to body

2) Does not account for broken HTML

3) Doesn't account for special tags such as <strong> or <h1>
'''


'''
INFORMATION FOR INVERTED INDEX:

Term, document frequency, document ID and term frequency

    i.e. Irvine 2 [(2,1), (4, 4)]

The word Irvine appears in two documents. In document 2, it appears once. In document 4 it appears 4 times.
Document ID can be a number or a URL (We choose).

'''

# Take the inverted index dictionary and output the information (in a clean and compact way) into a file.

def create_index_file(index, destination):
    ''' 
    Assumming Dictionary is of the form:
        {'Irvine': [docinfo, docinfo, ...]}
        docinfo: doc_ID, term_frequency, and special
    '''  
    
    file_name = 'inverted_index.txt'
    file_path = destination + file_name
    
    with open(file_path, 'w') as file:

        #Iterate through inverted index dictionary
        for term, information in index.items():
            document_frequency = len(information) # Number of files the term appeared in
            index_structure = term + ' ' + str(document_frequency) + ': ' #Represents a line in the output file
            listing = [(info.docID, info.term_frequency) for info in information] #Information about term in each doc
            index_structure += str(listing) + '\n'

            file.write(index_structure.encode('utf-8'))

#Words to not include in our inverted index
stop_words = ('a', 'around', 'and', 'every', 'for', 'from', 'in' \
              'is', 'it', 'not', 'on', 'one', 'the', 'to', 'under')

index = dict() #Inverted Index

# Iterate through corpus
for root, dirs, files in os.walk("./WEBPAGES_CLEAN_TEST"):
    
    #Iterater through each webpage in the corpus
	for name in files:
		document = os.path.join(root,name)
		# print("docid: " + document) #./WEBPAGES_CLEAN\0\102

		#file_content = open(document, encoding = 'utf-8').read() #Gave me an error about encoding, python 2.7 - A.V.
		file_content = codecs.open(document, 'r', encoding='utf-8').read()
        
        # For fixing broken HTML.
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
        
        # Find term inside the <strong> tag
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

        # Find terms inside the <body> tag
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


	
#FOR TENSTING
'''
	for keys,values in index.items():
	    # print("keys " + str(keys))
	    # for k in values:
	    # 	print("value: " + str(k))
	    # print('\n')
	    if keys == "hello":
	    	for i in values:
	    		print(i)

'''
create_index_file(index, '/home/s4x5/Documents/github/SearchEngine/')

		# for t in soup.find_all('strong'):

			
		# print(soup.get_text())

		# print(content)

		# tokens = nltk.word_tokenize(file_content)
		# print(tokens)
		# # except:
		# # 	pass
