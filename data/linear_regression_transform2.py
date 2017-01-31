import csv

from dateutil.parser import parse


def transform(ticker, no_today):
    with open('tickers/' + ticker + '.csv') as csvfile:
        # skip first row
        next(csvfile, None)
        if no_today is 0:
            f = open('volume/' + ticker + '.csv', 'w')
        elif no_today is 1:
            # skip first row
            next(csvfile, None)
            f = open('volume/' + ticker + '_no_today.csv', 'w')
        elif no_today is 2:
            f = open('volume/' + ticker + '_only_today.csv', 'w')

        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            date = row[0]
            volume= row[5]
            b = parse(date)
            time_slot = str(736311 - b.toordinal())
            new_row = volume + " " + "1:" + time_slot + ' \n'
            # print(new_row)
            f.write(new_row)
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
