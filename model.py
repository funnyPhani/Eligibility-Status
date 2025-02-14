# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 09:08:03 2019

@author: KIRAN
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_excel('eligibility.xlsx')

dataset['Experience'].fillna(0, inplace=True)

dataset['Assessment score'].fillna(dataset['Assessment score'].mean(), inplace=True)

X = dataset.iloc[:, :3]

#Converting words to integer values
def convert_to_int(word):
    word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
                'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0, 0: 0}
    return word_dict[word]

dataset['Experience'] = dataset['Experience'].apply(lambda x : convert_to_int(x))
dataset['Eligibility'] = dataset['Eligibility'].map({'Yes': 1, 'No': 0})

y = dataset.iloc[:, -1]

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2, 9, 6]]))