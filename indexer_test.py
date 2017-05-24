from nltk.tokenize import RegexpTokenizer
import codecs
import os
from bs4 import BeautifulSoup
import document_information as di
import re
from collections import Counter

'''
INFORMATION FOR INVERTED INDEX:

Term, document frequency, document ID and term frequency

    i.e. Irvine 2 [(2,1), (4, 4)]

The word Irvine appears in two documents. In document 2, it appears once. In document 4 it appears 4 times.
Document ID can be a number or a URL (We choose).

'''


# Take the inverted index dictionary and output the information (in a clean and compact way) into a file.

def output_index(index, destination):
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

            file.write(index_structure.encode('utf-8')) #Write information into file

def find_body(index, soup, tokenizer, document):

    #Find terms inside <body> tag

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

def find_strong(index, soup, tokenizer, document):
    # UNCOMMENT STRONG TAGS AND HEADING TAGS TO INDEX THOSE
    
    # Find terms inside <strong> tags 

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
    pass

def find_heading(index, soup, tokenizer, document):
    #HEADING TAGS

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
    pass

def create_index():
   
    index = dict() #list of objects
    strong_index = dict() #list of tuples
    heading_index = dict() #list of tuples

    for root, dirs, files in os.walk("./WEBPAGES_CLEAN"):

        for name in files:
        
            document = os.path.join(root,name)

            #soup = BeautifulSoup(open(document, encoding = 'utf-8').read(), "html.parser") #Error about encoding - A.V.
            soup = BeautifulSoup(codecs.open(document, encoding = 'utf-8').read(), "html.parser")

            tokenizer = RegexpTokenizer(r'\w+')
            
            find_body(index, soup, tokenizer, document)
            #find_strong(strong_index, soup, tokenizer, document)
            #find_headind(heading_index, soup, tokenizer, document)
            

    #Combine indexes and return
    return index

#For testing
'''
for keys,values in index.items():
    # print("keys " + str(keys))
    # for k in values:
    # 	print("value: " + str(k))
    # print('\n')

    if keys == "irvine":
    	print(keys)
    	print (len(values))

'''
if __name__ == '__main__':
    index = create_index()
    output_index(index, '/home/s4x5/Documents/github/SearchEngine/')
