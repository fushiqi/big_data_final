import csv

from dateutil.parser import parse


def transform(ticker, no_today):
    with open('tickers/' + ticker + '.csv') as csvfile:
        # skip first row
        next(csvfile, None)
        if no_today is 0:
            f = open('newlr/' + ticker + '.csv', 'w')
        elif no_today is 1:
            # skip first row
            next(csvfile, None)
            f = open('newlr/' + ticker + '_no_today.csv', 'w')
        elif no_today is 2:
            f = open('newlr/' + ticker + '_only_today.csv', 'w')

        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            date = row[0]
            close_price = row[4]
            volume = row[5]
            b = parse(date)
            time_slot = str(736311 - b.toordinal())
            
          
            new_row = close_price + " " + "1:" + time_slot + " " + "2:" + volume + ' \n'
            # print(new_row)
            f.write(new_row)
           # f.write(new_row[0])
            if no_today is 2:
                break

    f.close()


def transform_all():
    with open('../data/ticker_list.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            ticker = row[0]
            # print(ticker)
            transform(ticker, 0)  # all
            transform(ticker, 1)  # no today
            transform(ticker, 2)  # only today


if __name__ == '__main__':
    transform_all()
