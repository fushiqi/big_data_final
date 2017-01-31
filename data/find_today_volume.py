import csv


with open("../data/tickers/"+ticker+".csv") as csvfile:
	reader = csv.reader(csvfile, delimiter=',',quotechar='|')
	count=0
	for row in reader:
		if count==1:
			today_volume=row[5]
			count=count+1
		else:
			count=count+1
print(today_volume)
