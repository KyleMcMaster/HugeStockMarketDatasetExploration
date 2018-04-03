# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 14:30:27 2018

@author: kyler
"""
#import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# load dataset (assume wdir is root of git project folder)
filename = 'aapl.us.txt'
dataset = pd.read_csv('Data/stocks/' + filename)

#just going to look at the difference in price between open and close from 2008 forward
dataset = dataset[(dataset['Date'] >= '2008-01-01')]
dataset['PriceDiff'] = dataset['Close'] - dataset['Open']

#let's take a look at price difference between open and close over time
plt.scatter(dataset['Date'], dataset['PriceDiff'], color = 'red')
plt.title('AAPL change in price daily')
plt.xlabel('Date')
plt.ylabel('Change in Price')
plt.show()
plt.clf()

#do the same thing high and low
dataset = dataset[(dataset['Date'] >= '2008-01-01')]
dataset['PriceDiff'] = dataset['High'] - dataset['Low']

#let's take a look at price difference between open and close over time
plt.scatter(dataset['Date'], dataset['PriceDiff'], color = 'red')
plt.title('AAPL difference between high and low daily')
plt.xlabel('Date')
plt.ylabel('Difference in Price')
plt.show()
