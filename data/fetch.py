import urllib

import csv


def download_tickers():
    testfile = urllib.URLopener()
    with open('ticker_list.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            ticker = row[0]
            # get tickers
            try:
                testfile.retrieve(
                    "http://chart.finance.yahoo.com/table.csv?s=" + ticker + "&a=09&b=13&c=2016&d=11&e=13&f=2016&g=d&ignore=.csv",
                    "./tickers/" + ticker + ".csv")
            except:
                print(ticker)


def get_ticker_list():
    f = open('ticker_list.csv', 'w')
    with open('sp500-components.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            ticker = row[0] + '\n'
            f.write(ticker)
            # get tickers
    f.close()


if __name__ == '__main__':
    download_tickers()
