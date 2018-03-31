# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 19:12:13 2018

@author: kylermcmaster@gmail.com

    
"""

#import libraries
import pandas as pd
import matplotlib.pyplot as plt

# load dataset (assume wdir is root of git project folder)
AAPLFileName = 'aapl.us.txt'
AAPLData = pd.read_csv('Data/stocks/' + AAPLFileName)

TSLAFileName = 'tsla.us.txt'
TSLAData = pd.read_csv('Data/stocks/' + TSLAFileName)

#plot close price over time
plt.scatter(AAPLData['Date'], AAPLData['Close'], color = 'red')
plt.scatter(TSLAData['Date'], TSLAData['Close'], color = 'blue')
plt.title('AAPL vs TSLA Close Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
plt.clf()

#plot cose price over time starting from tesla go live date
AAPLDataTrunc = AAPLData[AAPLData['Date'].isin(TSLAData['Date'])] # get all AAPLData that is in TSLA
plt.scatter(AAPLDataTrunc['Date'], AAPLDataTrunc['Close'], color = 'red')
plt.scatter(TSLAData['Date'], TSLAData['Close'], color = 'blue')
plt.title('AAPL vs TSLA Close Prices Truncated')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
plt.clf()

#let's take a look at volume over time
plt.scatter(AAPLData['Date'], AAPLData['Volume'], color = 'red')
plt.title('AAPL Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.show()
plt.clf()