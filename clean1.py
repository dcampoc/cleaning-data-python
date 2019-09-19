# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 01:02:06 2019

@author: dcamp
"""
import pandas as pd 
import os
os.chdir(r'C:\Users\dcamp\Documents\python-practice\Cleaning-data')
# tuberculosis dataset values 
tb = pd.read_csv('tb.csv')
# Print the head of tb_melt
print('tidy data: Each column should represent a variable'.upper)

# m014 means m:masculine and 014 means an age group form 0 to 14 years old
print(tb.head())

# Melt tb keeping 'country' and 'year' fixed and merge the rest of the columns into one 
# Melt tb: tb_melt
tb_melt = pd.melt(tb, id_vars=['country', 'year'])

# Create the 'gender' column 
# Create a 'gender' column by slicing the first letter of the variable column of tb_melt
tb_melt['gender'] = tb_melt.variable.str[0]

# Create the 'age_group' column
# Create an 'age_group' column by slicing the rest of the variable column of tb_melt.
tb_melt['age_group'] = tb_melt.variable.str[1:]

# Print the head of tb_melt
print(tb_melt.head())


#####################
import numpy as np
# tips dataset values 
tips = pd.read_csv('tips.csv')

# Define recode_gender()
def recode_gender(gender):

    # Return 0 if gender is 'Female'
    if gender == 'Female':
        return 0
    
    # Return 1 if gender is 'Male'    
    elif gender == 'Male' :
        return 1
    
    # Return np.nan    
    else:
        return np.nan

# Apply the function to the sex column
tips['recode_gender'] = tips.sex.apply(recode_gender)

# Print the first five rows of tips
print(tips.head())




