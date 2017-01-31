import urllib
import csv

testfile = urllib.URLopener()
with open('ticker_list.csv') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader:
		ticker = row[0]
		with open("../data/lr/"+ ticker + "_no_today.csv") as csvfile2:
			reader2=csv.reader(csvfile2, delimiter=',')
			#rows=[row for row in reader2]
			csvfile3 = file('lr2/' + ticker+'only10.csv','wb')
			writer=csv.writer(csvfile3)
			j=1
			for row in reader2:
				if j<11:
					newrow = row
					writer.writerow(newrow)
					j=j+1
				
				