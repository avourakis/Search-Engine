import mmap
import os
import re
import csv
import serialization as sr
import json

def main():

	word = "Informatics"

	# tsv = open('C:\SCHOOL\INF 141\SearchEngine\WEBPAGES_CLEAN\\bookkeeping.tsv')

	filename = 'inverted_index.pickle'
	inverted_index = sr.extract_index(filename)

	docs = [] #list of './WEBPAGES_CLEAN\\43\\436'

	word = word.lower()

	for i in inverted_index[word]:
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
	main()
