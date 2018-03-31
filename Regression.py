# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 22:06:08 2018

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

#take the average of the Open, High, Low, Close values to give an average price for the day
dataset['Price'] = (dataset['Open'] + dataset['High'] + dataset['Low'] + dataset['Close']) / 4

#create X and Y variables
X = dataset['Date']
Y = dataset['Price']

#encodes the date column using LabelEncoder
le_X = LabelEncoder()
X = le_X.fit_transform(X)
X = X.reshape(-1, 1)

#train test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

#fit model to the dataset
poly_reg = PolynomialFeatures(degree = 8)
X_poly = poly_reg.fit_transform(X_train)
poly_reg.fit(X_poly, Y_train)
regressor = LinearRegression()
regressor.fit(X_poly, Y_train)

#visualize the predictions
plt.scatter(X_test, Y_test, color = 'red')
plt.scatter(X_test, regressor.predict(poly_reg.fit_transform(X_test)), color = 'blue')
plt.title('AAPL Stock Predictions')
plt.ylabel('price')
plt.xlabel('date (encoded)')
plt.show()