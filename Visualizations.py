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
plt.ylabel('price')
plt.xlabel('date')
plt.show()

