from __future__ import print_function, division

from pyspark.sql import SparkSession
from pyspark.ml.regression import GeneralizedLinearRegression

import csv


def linear_regression(ticker,writer):
    spark = SparkSession \
        .builder \
        .appName("GeneralizedLinearRegressionExample") \
        .getOrCreate()
    # Load training data
    dataset = spark.read.format("libsvm").load("../data/lr/" + ticker + "_no_today.csv")
    glr = GeneralizedLinearRegression(family="gaussian", link="identity", maxIter=1, regParam=0.8)

    # Fit the model
    model = glr.fit(dataset)
    data=[ticker, 'coefficient:', model.coefficients[0],'intercept:',model.intercept]
    writer.writerow(data)
    print(data)
    # predict
    today_close_value = 0
    yesterday_close_value = 0
    with open("../data/lr/" + ticker + ".csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        count = 0
        for row in reader:
            if count is 0:
                today_close_value = row[0]
                count += 1
            elif count is 1:
                yesterday_close_value = row[0]
                break

    # # print(today_close_value)
    # # print(yesterday_close_value)

    predict_close_value = -1 * float(str(model.coefficients[0])) + float(str(model.intercept))
    # print(predict_close_value)
    spark.stop()
    if predict_close_value >= yesterday_close_value and today_close_value >= yesterday_close_value:
        return True
    elif predict_close_value <= yesterday_close_value and today_close_value <= yesterday_close_value:
        return True
    else:
        return False


# def get_accuracy():
#     true_positive = 0
#     total = 0
#     csvfile3 = file('../data/result/' + 'alg1result2.csv','wb')
#     writer = csv.writer(csvfile3)

#     with open('../data/ticker_list.csv') as csvfile:
#         reader = csv.reader(csvfile, delimiter=',', quotechar='|')
#         for row in reader:
#             print(row[0])
#             total += 1
#             flag = linear_regression(row[0],writer)
#             if flag is True:
#                 true_positive += 1
#     print(true_positive / total)
#     return true_positive / total

def get_accuracy():
    true_positive = 0
    total = 0
    f = open('result_lr.csv', 'w')
    csvfile3 = file('../data/result/' + 'alg1result2.csv','wb')
    writer = csv.writer(csvfile3)
    with open('../data/ticker_list.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')

        for row in reader:
            print(row[0])
            total += 1
            flag = linear_regression(row[0], writer)
            if flag is True:
                true_positive += 1
                f.write(row[0] + '\n')
    f.close()
    return true_positive / total


if __name__ == '__main__':
    get_accuracy()
       
# if __name__ == '__main__':
#     # get_accuracy()
#     csvfile3 = file('../data/result/' + 'alg1result2.csv','wb')
#     writer = csv.writer(csvfile3)
#     linear_regression("AAL", writer)