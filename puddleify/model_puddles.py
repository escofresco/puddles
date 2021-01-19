
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


# cleaning data
def data_cleanse(data_file):

    # grab the csv file make it a dataframe
    df = pd.read_csv(data_file)

    # remove a column
    # df.drop('0', inplace=True, axis=1)

    # remove missing values by creating a new dataset
    # df_no_missing = df.loc[(df['column'] != '?')
    #                       & (df['column2'] != '?2')]
    # print(df.head())

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
    # print('X HEAD ')
    # print(X.head())
    # print('X.  ', X.dtypes)

    # the column we want to predict in Y
    y = df['puddle'].copy()
    # print('y HEAD ')
    # print(y.head())
    # print('Y.  ', y.dtypes)

    return ([X, y])

# sci kit learn doesn't natively support categorical data, thus...
def one_hot_encoding(ex_wai):

    X = ex_wai[0]
    y = ex_wai[1]
    
    X_encoded = pd.get_dummies(X, columns=['category', 'date', 'name', 'orginal_description', 'address', 'city', 'state'])
    # print('1X_encoded:')
    # print(X_encoded.head())

    y_encoded = pd.get_dummies(y, columns=['puddles'])
    # print('1y_encoded: ')
    # print(y_encoded.head())

    return ([X_encoded, y_encoded])

def train_data(ex_wai_encoded):

    assert len(ex_wai_encoded) == 2, 'Length of encoded training data'

    X_enco = ex_wai_encoded[0]
    y_enco = ex_wai_encoded[1]

    # print('2x encoded: ')
    # print(X_enco)
    # print('2y encoded: ')
    # print(y_enco)

    X_train, X_test, y_train, y_test = train_test_split(X_enco, y_enco, random_state=42)

    clf_dt = DecisionTreeClassifier(random_state=42)
    clf_dt = clf_dt.fit(X_train, y_train)

    plt.figure(figsize=(15, 7.5))
    plot_tree(clf_dt, filled=True, rounded=True, class_names=["Puddle 1", "Puddle 2", "Puddle 3", "Puddle 4"], feature_names=X_enco.columns);

    return




if __name__ == '__main__':

    cleansed = data_cleanse('testing.csv')
    formatted = decision_tree_formatter(cleansed)
    encoded = one_hot_encoding(formatted)
    tree = train_data(encoded)