
# Take training dataset from feature engineering, pass through models. 
# Test models and accuracy

# We'll use sci-kit learn's Decision Tree / Random Forests to classify the puddles

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import confusion_matrix, plot_confusion_matrix