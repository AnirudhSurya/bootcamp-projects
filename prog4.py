import csv
with open('names.csv',newline='') as csvfile:
	spamreader=csv.reader(csvfile)
	for row in spamreader:
		print(', '.join(row))
