#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import print_function

from pyspark.sql import SparkSession
# $example on$
from pyspark.ml.regression import GeneralizedLinearRegression
# $example off$
import csv
"""
An example demonstrating generalized linear regression.
Run with:
  bin/spark-submit examples/src/main/python/ml/generalized_linear_regression_example.py
"""

def linear_regression(ticker,writer):
    spark = SparkSession\
        .builder\
        .appName("GeneralizedLinearRegressionExample")\
        .getOrCreate()

    # $example on$
    # Load training data
    dataset1 = spark.read.format("libsvm")\
        .load("../data/volume2/" + ticker + "only10.csv")

    glr1 = GeneralizedLinearRegression(family="gaussian", link="identity", maxIter=1, regParam=0.3)

    # Fit the model
    model1 = glr1.fit(dataset1)

    # Print the coefficients and intercept for generalized linear regression model
    Coefficients1 = model1.coefficients

    # Summarize the model over the training set and print out some metrics
    dataset2 = spark.read.format("libsvm")\
        .load("../data/lr2/" +  ticker + "only10.csv")

    glr2 = GeneralizedLinearRegression(family="gaussian", link="identity", maxIter=1, regParam=0.3)

    # Fit the model
    model2 = glr2.fit(dataset2)

    # Print the coefficients and intercept for generalized linear regression model
    Coefficients2 = model2.coefficients

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


    spark.stop()

    if (Coefficients1 < 0 or Coefficients2 < 0):
        writer.writerow(row[0]+": the stock would be bullish")
    else:
        writer.writerow(row[0]+": the stock would be bearish")


    if (Coefficients1 < 0 or Coefficients2 < 0) and (today_close_value >= yesterday_close_value):
        return True
    elif (Coefficients1 > 0 or Coefficients2 > 0) and (today_close_value <= yesterday_close_value):
        return True
    else:
        return False
    

def get_accuracy():
    true_positive = 0
    total = 0
    csvfile3 = file('../data/result/' + 'alg2result.csv','wb')
    writer = csv.writer(csvfile3)
   
    with open('../data/ticker_list.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            print(row[0])
            total += 1
            flag = linear_regression(row[0],writer)
            if flag is True:
                true_positive += 1
                
    print("accuracy = :", true_positive / total)
    return true_positive / total


if __name__ == '__main__':
    get_accuracy()
       




