# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 01:17:56 2019

@author: dcamp
"""

import pandas as pd 
import os
os.chdir(r'C:\Users\dcamp\Documents\python-practice\Cleaning-data')

df = pd.read_csv('nyc_uber_2014.csv')
# Split data
uber1 = df.loc[:98,:]
uber2 = df.loc[99:99+98,:]
uber3 = df.loc[198:,:]

# Row concatenation uber1, uber2, and uber3: row_concat
row_concat = pd.concat([uber1, uber2, uber3], axis=0)

# Print the shape of row_concat
print(row_concat.shape)

# Print the head of row_concat
print(row_concat.head())

########## Using regular expressions 
import re
# The pattern recognizes as True, values that have dollar sign at the begining, then an arbitrary number of digits *, a point and two decimals
# ^ indicates the start of the pattern and $ represents the end of the pattern 
pattern = re.compile('^\$\d*\.\d{2}$')
result_0 = pattern.match('$17.89')
result_1 = pattern.match('8.89')
result_2 = pattern.match('$1.894')
result_3 = pattern.match('$1.0')
result_4 = pattern.match('$1.00')

print(bool(result_0))
print(bool(result_1))
print(bool(result_2))
print(bool(result_3))
print(bool(result_4))

# Find the numeric values: matches
matches = re.findall('\d+', 'the recipe calls for 10 strawberries and 1 banana')

# Print the matches
print(matches)

