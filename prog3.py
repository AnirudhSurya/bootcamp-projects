import csv
with open('names.csv','w',newline='') as csvfile:
	spamwriter=csv.writer(csvfile)	
	spamwriter.writerow(['ani']*5+['amogh'])
	spamwriter.writerow(['kk','adi','akhil'])
