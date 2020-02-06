#!/usr/bin/env python
# coding: utf-8

import pandas
import matplotlib.pyplot as plt


# 1
def plotHistograms(df):
    for chart_title in df.columns[0:12]:
        df[chart_title].hist(bins=10)
        plt.axvline(df[chart_title].mean())
        plt.ylabel('Frequency')
        plt.xlabel(chart_title)
        plt.title('Frequency of ' + chart_title + ': Histogram Plot')
        plt.show()


# 2
def featureScatterPlot(df):
    corrMatrix = df.corr()

    corrMatrix.to_html("./data/correlationMatrixResults.html")
    ##We can see here that Total Surfur Dioxide and Total Sulfur Dioxide


# 3
def correlatedScatterPlot(df):
    ##From the previous correlation matrix, we can see that quality and alcohol have a .444 correlation. Which is strongest.
    df.plot.scatter(x='quality', y='alcohol')
    plt.show()


# 4
def calculateAvgAlcoholContent(df):
    df.groupby('quality')['alcohol'].mean()
    # print(df)
    frameQualityMax = df[(df.quality == df.quality.max())]
    # print(frameQualityMax)
    avg_alcohol_for_best_wine = frameQualityMax['alcohol'].mean()
    print(f'The average alcohol content for best wine is {avg_alcohol_for_best_wine}.')


# 5
def calculateCorrelationCoefficients(df):
    df.groupby('wine type').corr()

    df[(df.wine_type == 'Red')].plot.scatter(x='quality', y='fixed acidity', )
    plt.title('Red')

    df[(df.wine_type == 'White')].plot.scatter(x='quality', y='fixed acidity', )
    plt.title('White')


df = pandas.read_csv('./Data/winequality.csv', encoding="ISO-8859-1")
df = df.drop(df.columns[0], axis=1)

#plotHistograms(df) ##1
featureScatterPlot(df) ##2
#correlatedScatterPlot(df)  ##3
# calculateAvgAlcoholContent(df)  ##4
# calculateCorrelationCoefficients(df) ##5
