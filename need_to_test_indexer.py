from nltk.tokenize import RegexpTokenizer
import os
import codecs
from bs4 import BeautifulSoup
import document_information as di
import re
from collections import Counter
import serialization as sr

'''
INFORMATION FOR INVERTED INDEX:

Term, document frequency, document ID and term frequency

    i.e. Irvine 2 [(2,1), (4, 4)]

The word Irvine appears in two documents. In document 2, it appears once. In document 4 it appears 4 times.
Document ID can be a number or a URL (We choose).

'''

#Words to not include in our inverted index
STOP_WORDS = ('a', 'around', 'and', 'every', 'for', 'from', 'in' \
              'is', 'it', 'not', 'on', 'one', 'the', 'to', 'under')

# Take the inverted index dictionary and output the information (in a clean and compact way) into a file.

def compress_index(index, target_folder, file_name):
    return sr.compress_index(index, target_folder, file_name)

def output_index(index, destination):
    ''' 
    Assumming Dictionary is of the form:
        {'Irvine': [docinfo, docinfo, ...]}
        docinfo: doc_ID, term_frequency, and special
    '''  
    
    file_name = 'inverted_index.txt'
    file_path = destination + file_name
    
    with open(file_path, 'wb') as file:

        #Iterate through inverted index dictionary
        for term, information in index.items():
            document_frequency = len(information) # Number of files the term appeared in
            index_structure = term + ' ' + str(document_frequency) + ': ' #Represents a line in the output file
            listing = [(info.docID, info.term_frequency) for info in information] #Information about term in each doc
            index_structure += str(listing) + '\n'

            file.write(index_structure.encode('utf-8')) #Write information into file

def find_strong(index, soup, tokenizer, document):
    # UNCOMMENT STRONG TAGS AND HEADING TAGS TO INDEX THOSE

    #Find terms inside <strong> and <b> tags 

    tokens = []

    for content in soup.find_all(['strong','b']):
        for term in tokenizer.tokenize(content.text):
            term = term.lower()
            tokens.append(term)

    counts = Counter(tokens)

    #create separate index
    for k,v in counts.items():
        if k not in index:
            index[k] = set()
        
        #when term exists in dictionary add a value to special
        for doc in index[k]:
            if doc.docID == document:
                doc.special += 4 #May need to give a different score. It has to match the type of score given when weighting 

def find_heading(index, soup, tokenizer, document):
    #HEADING TAGS

    #Find terms inside <h1> tags 

    tokens = []

    for content in soup.find_all('h1'):
        for term in tokenizer.tokenize(content.text):
            term = term.lower()
            tokens.append(term)

    counts = Counter(tokens)

    #create separate index
    for k,v in counts.items():
        if k not in index:
            index[k] = set()
        
        #when term exists in dictionary add a value to special
        for doc in index[k]:
            if doc.docID == document:
                doc.special += 1 #May need to give a different score. It has to match the type of score given when weighting 

    #Find terms inside <h2> tags 

    tokens = []

    for content in soup.find_all('h2'):
        for term in tokenizer.tokenize(content.text):
            term = term.lower()
            tokens.append(term)

    counts = Counter(tokens)

    #create separate index
    for k,v in counts.items():
        if k not in index:
            index[k] = set()
        
        #when term exists in dictionary add a value to special
        for doc in index[k]:
            if doc.docID == document:
                doc.special += 2 #May need to give a different score. It has to match the type of score given when weighting 

    tokens = []

    for content in soup.find_all('h3'):
        for term in tokenizer.tokenize(content.text):
            term = term.lower()
            tokens.append(term)

    counts = Counter(tokens)

    #create separate index
    for k,v in counts.items():
        if k not in index:
            index[k] = set()
        
        #when term exists in dictionary add a value to special
        for doc in index[k]:
            if doc.docID == document:
                doc.special += 3 #May need to give a different score. It has to match the type of score given when weighting 




def find_body(index, soup, tokenizer, document):
    #Find terms inside <body> tag

    global STOP_WORDS
    tokens = [] #all the tokens in the body

    #missing opening tags were messing with the way our indexer found text within <body>
    #so i changed it to not find body, but all text excluding tags
    #basically, this ignores when there is a missing open tag now

    content = soup.get_text()
    for term in tokenizer.tokenize(content):
        if term not in STOP_WORDS: #Prevent stop words from being indexed
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


def create_index():
   
    index = dict() #list of objects

    for root, dirs, files in os.walk("./WEBPAGES_CLEAN"):

        for name in files:

            document = os.path.join(root,name)

            with open(document, encoding = "utf-8") as file:
                soup = BeautifulSoup(file.read(), "html.parser")

                # print(soup.prettify())

                tokenizer = RegexpTokenizer(r'\w+')
                
                find_body(index, soup, tokenizer, document)
                find_strong(index, soup, tokenizer, document)
                find_heading(index, soup, tokenizer, document)
        
    #Combine indexes and return
    return index

if __name__ == '__main__':
    # folder =  '/home/s4x5/Documents/github/SearchEngine/' #Andres 
    folder = 'C:\SCHOOL\INF 141\SearchEngine\\' #shirby
    index = create_index()
    #output_index(index, folder) #Andres 
    compress_index(index, folder, 'inverted_index') #AKA Pickle the index!



