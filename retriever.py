import mmap
import os
import re
import csv
import serialization as sr
import json

def extract_index(file_name):
    print('Loading Inverted Index... \n')
    inverted_index = sr.extract_index(file_name)
    print('Inverted Index has been loaded \n')
    return inverted_index

def user_input():
    return input('What would you like to search for? ').lower()

def retrieve():

    # tsv = open('C:\SCHOOL\INF 141\SearchEngine\WEBPAGES_CLEAN\\bookkeeping.tsv')
    file_name = 'inverted_index.pickle'
    inverted_index = extract_index(file_name)

    query = user_input()

    docs = [] #list of './WEBPAGES_CLEAN\\43\\436'

    for i in inverted_index[query]:
        d = i.docID
        dl= [str(x) for x in re.findall(r'\b\d+\b', d)]
        docs.append(dl[0] + '/' + dl[1])

    #order by tf-idf at one point

    result_urls = []

    with open('C:\SCHOOL\INF 141\SearchEngine\WEBPAGES_CLEAN\\bookkeeping.json') as json_data:
        jd = json.load(json_data)
        for doc in docs:
            result_urls.append(jd[doc])

if __name__ == "__main__":
	retrieve()
