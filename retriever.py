import mmap
import os
import re
import csv

def main():

	word = "genomes"

	filename = 'inverted_index.txt'
	f = open('inverted_index.txt' , 'r')

	tsv = open('C:\SCHOOL\INF 141\SearchEngine\WEBPAGES_CLEAN\\bookkeeping.tsv')

	docs = []

	for line in f.readlines(): #for each key/value pair
		item = line.split(' ')
		if item[0] == word: #found key that we are looking for
			print(word + " : " + item[1])
			for i in item[2:][::2]: #iterate through every docinfo objects to skip the doc frequency
				doc = [str(x) for x in re.findall(r'\b\d+\b', i)]
				docs.append(doc)

	# print(docs)

	result_urls = []

	for doc in docs:
		for line in csv.reader(tsv, dialect="excel-tab"):
			csvdoc = line[0].split('/')
			if doc == csvdoc: #if doc in inverted_index matches the one in bookkeeping
				result_urls.append(line[1]) #the urls!
		tsv.seek(0)

	print(result_urls)

		# bleh stuff

		# if item[0] == 'informatics':
		# 	print("informatics: " + item[1])
		# if item[0] == 'mondego':
		# 	print("mondego: " + item[1])
		# if item[0] == 'irvine':
		# 	print("irvine: " + item[1])

	# s = mmap.mmap(f.fileno(), 0, access = mmap.ACCESS_READ)
	# begin = s.find(b' irvine ')
	# print(begin)
	# s.seek(begin)
	# end = s.find(b']')
	# print(begin)
	# print(end)
	# print(s[begin:end])


if __name__ == "__main__":
	main()
