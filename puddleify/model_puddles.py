
# Take training dataset from feature engineering, pass through models. 
# Test models and accuracy

# We'll use sci-kit learn's Decision Tree / Random Forests to classify the puddles
import json 
import csv 
  
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import confusion_matrix, plot_confusion_matrix

# be able to accept JSON data, turn it into a csv file
def json_to_csv():
    # Opening JSON file and loading the data 
    # into the variable data 
    with open('data.json') as json_file: 
        data = json.load(json_file) 
    
    json_data = data['emp_details'] 
    
    # now we will open a file for writing 
    data_file = open('data_file.csv', 'w') 
    
    # create the csv writer object 
    csv_writer = csv.writer(data_file) 
    
    # Counter variable used for writing  
    # headers to the CSV file 
    count = 0
    
    for item in json_data: 
        if count == 0: 
    
            # Writing headers of CSV file 
            header = item.keys() 
            csv_writer.writerow(header) 
            count += 1
    
        # Writing data of CSV file 
        csv_writer.writerow(item.values()) 
    
    data_file.close() 



# cleaning data
def data_cleanse(data_file):

    # grab the csv file make it a dataframe
    df = pd.read_csv(data_file)

    # remove a column
    df.drop('0', inplace=True, axis=1)

    # remove missing values by creating a new dataset
    # df_no_missing = df.loc[(df['column'] != '?')
    #                       & (df['column2'] != '?2')]
    print(df.head())

    # unique values
    # print(df['amount'].unique())

    # guess? 
    return df

def decision_tree_formatter(df):
    ''' Once the data has been cleansed, format it here so it's prepared for the treee
    This splits the data into train and split '''

    # all the coliumns we want to train on in X
    # print(df.head())
    X = df.iloc[:, :-1]
    # print('X HEAD ', X.head())
    print(X.dtypes)

    # the column we want to predict in Y
    y = df['puddle'].copy()
    # print('y HEAD ', y.head())
    print(y.dtypes)

    return ([X, y])

# sci kit learn doesn't natively support categorical data, thus...
def one_hot_encoding():

    pass


if __name__ == '__main__':

    cleansed = data_cleanse('testing.csv')
    # formatted = decision_tree_formatter(cleansed)