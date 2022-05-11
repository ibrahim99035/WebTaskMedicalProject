#import modules
import pandas as pd 
import numpy as np 

import random
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import accuracy_score, classification_report

# for Machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import StackingClassifier

import pickle

# To ignore unwanted warnings
import warnings
warnings.filterwarnings('ignore')
#------------------------------------------------------------------------------------
#load and splite data
# Load dataset into the memory

data = pd.read_csv('data-ori.csv')
#------------------------------------------------------------------------------------
# Label encoding
# (1=in care patient), (0=out care patient)
# data['SOURCE'] = np.where(data['SOURCE'] == 'F', 0, 1)
# data['SOURCE'] = data.SOURCE.replace({"in":1, 'out':0}, inplace=True)
data['SOURCE'].mask(data['SOURCE'] == 'F', 0, inplace=True)





























