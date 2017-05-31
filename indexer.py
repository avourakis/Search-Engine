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


def create_index():
   
    index = dict() #list of objects

    for root, dirs, files in os.walk("./WEBPAGES_CLEAN"):

        for name in files:
        
            document = os.path.join(root,name)

            soup = BeautifulSoup(open(document, encoding = "utf-8").read(), "html.parser")

            tokenizer = RegexpTokenizer(r'\w+')
            
            find_body(index, soup, tokenizer, document)
            #find_strong(strong_index, soup, tokenizer, document)
            #find_headind(heading_index, soup, tokenizer, document)
            

    #Combine indexes and return
    return index

if __name__ == '__main__':
    # folder =  '/home/s4x5/Documents/github/SearchEngine/' #Andres 
    folder = 'C:\SCHOOL\INF 141\SearchEngine\\' #shirby
    index = create_index()
    #output_index(index, folder) #Andres 
    compress_index(index, folder, 'inverted_index')



