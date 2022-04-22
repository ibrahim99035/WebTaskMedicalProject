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

data = pd.read_csv('kaggleDataset/data-ori.csv')
#------------------------------------------------------------------------------------
# Label encoding
# (1=in care patient), (0=out care patient)
data['SOURCE'] = data.SOURCE.replace({"in":1, 'out':0})


# get all the features
features = [feat for feat in data.columns if feat !='SOURCE']

X = data[features] # feature set
y = data['SOURCE'] # target

# Splitting data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)
#---------------------------------------------------------------------------------------
print(f"The dataset contains {data.shape[0]} rows and {data.shape[1]} columns")

num_features = [feat for feat in features if data[feat].dtype != object]
cat_features = [feat for feat in features if data[feat].dtype == object]

print(f"Total number of features : {len(features)}")
print(f"Number of numerical features : {len(num_features)}")
print(f"Number of categorical features : {len(cat_features)}\n")
#------------------------------------------------------------------------------------------
# Replace labels of SEX with binary numbers

X_train.SEX.replace({'F':0, 'M':1}, inplace=True)
X_test.SEX.replace({'F':0, 'M':1}, inplace=True)

#-------------------------------------------------------------------------------------------
scaler = MinMaxScaler(feature_range=(0, 1))

X_train[num_features] = scaler.fit_transform(X_train[num_features]) #fit and transform the train set
X_test[num_features] = scaler.transform(X_test[num_features]) #transform the test test
#-------------------------------------------------------------------------------------------
# Remove least correlated features [MCH, MCHC, MCV]

X_train.drop(['MCH', 'MCHC','MCV'], axis=1, inplace=True)
X_test.drop(['MCH', 'MCHC','MCV'], axis=1, inplace=True)
#-------------------------------------------------------------------------------------------
#Decision Tree Classifier
tree = DecisionTreeClassifier(random_state=1)
tree.fit(X_train, y_train)

print("Train accuracy of DecisionTreeClassifier : ", accuracy_score(y_train, tree.predict(X_train)))
print("Test accuracy of DecisionTreeClassifier : ", accuracy_score(y_test, tree.predict(X_test)))

# Hyperparameters
distribution = {'max_depth': [4, 6, 8, 10, 12, 14, 16],
                'criterion': ['gini', 'entropy'],
                'min_samples_split': [2, 10, 20, 30, 40],
                'max_features': [0.2, 0.4, 0.6, 0.8, 1],
                'max_leaf_nodes': [8, 16, 32, 64, 128,256],
                'class_weight': [{0: 1, 1: 2}, {0: 1, 1: 3}, {0: 1, 1: 4}, {0: 1, 1: 5}]
               }

# Random search for best hyperparameters
search = RandomizedSearchCV(DecisionTreeClassifier(random_state=1),
                         distribution,
                         scoring='accuracy',
                         cv=3,
                         verbose=1,
                         random_state=1,
                         n_iter=30)

search.fit(X_train, y_train)

# Best parameters for DT classifier
print("Best parameters for DT classifier : ", search.best_params_)

# Retrain with best model

best_tree = search.best_estimator_

best_tree.fit(X_train, y_train)
print(" Best train accuracy for DT classifier : ", accuracy_score(y_train, best_tree.predict(X_train)))
print(" Best test accuracy for DT classifier : ", accuracy_score(y_test, best_tree.predict(X_test)))
print(classification_report(y_test, best_tree.predict(X_test)))
#-------------------------------------------------------------------------------------------
# Logistic Regression Classifier
logreg = LogisticRegression()

logreg.fit(X_train, y_train)

print("Train accuracy for Logistic Regression Classifier : ", accuracy_score(y_train, logreg.predict(X_train)))
print("Test accuracy for Logistic Regression Classifier : ", accuracy_score(y_test, logreg.predict(X_test)))
# Hyperparameters
param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
              'penalty':['l1', 'l2', 'elasticnet', 'none'],
              'fit_intercept':[True, False],
              'max_iter':[100, 200, 300],
              'class_weight': [{0: 1, 1: 1}, {0: 1, 1: 2}, {0: 1, 1: 4}, {0: 1, 1: 5}]
             }

# Random search for best hyperparameters
search = RandomizedSearchCV(LogisticRegression(random_state=1),
                         param_grid,
                         scoring='accuracy',
                         cv=3,
                         verbose=1,
                         random_state=1,
                         n_iter=30)

search.fit(X_train, y_train)

# Best parameters for Logistic regression classifier
print("Best parameters for Logistic Regression Classifier : ", search.best_params_)
# Retrain with best model

best_logreg = search.best_estimator_

best_logreg.fit(X_train, y_train)
print("Best train accuracy for Logistic Regression Classifier : ", accuracy_score(y_train, best_logreg.predict(X_train)))
print("Best test accuracy for Logistic Regression Classifier : ", accuracy_score(y_test, best_logreg.predict(X_test)))
print(classification_report(y_test, best_logreg.predict(X_test)))
#-------------------------------------------------------------------------------------------
#Support Vector Machine Classifier
svc = SVC(random_state=1)

svc.fit(X_train, y_train)

print("Train accuracy for Support Vector Machine Classifier : ", accuracy_score(y_train, svc.predict(X_train)))
print("Test accuracy for Support Vector Machine Classifier : ", accuracy_score(y_test, svc.predict(X_test)))

# Hyperparameters
param_grid = {'C': [0.1, 1, 10, 100, 1000], 
              'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
              'kernel': ['linear', 'rbf', 'poly'],
              'degree':[0, 1, 2, 3, 4, 5, 6]
             } 

# Random search for best hyperparameters
search = RandomizedSearchCV(SVC(random_state=1),
                         param_grid,
                         scoring='accuracy',
                         cv=3,
                         verbose=1,
                         random_state=1,
                         n_iter=30)

search.fit(X_train, y_train)

# Best parameters for Support vector classifier
print("Best parameters for Support Vector Machine Classifier : ", search.best_params_)
# Retrain with best model

best_svc = search.best_estimator_

best_svc.fit(X_train, y_train)
print("Best train accuracy for Support Vector Machine Classifier : ", accuracy_score(y_train, best_svc.predict(X_train)))
print("Best test accuracy for Support Vector Machine Classifier : ", accuracy_score(y_test, best_svc.predict(X_test)))
print(classification_report(y_test, best_svc.predict(X_test)))
#---------------------------------------------------------------------------------------------
#Random Forest Classifier
forest = RandomForestClassifier(random_state=1)

forest.fit(X_train, y_train)

print("Train accuracy for Random Forest Classifier : ", accuracy_score(y_train, forest.predict(X_train)))
print("Test accuracy for Random Forest Classifier : ", accuracy_score(y_test, forest.predict(X_test)))
# Hyperparameters
params_grid = {'bootstrap': [True, False],
             'max_depth': [2, 5, 10, 20, None],
             'max_features': ['auto', 'sqrt'],
             'min_samples_leaf': [1, 2, 4],
             'min_samples_split': [2, 5, 10],
             'n_estimators': [50, 100, 150, 200]}

# Random search for best hyperparameters
search = RandomizedSearchCV(RandomForestClassifier(random_state=1),
                         params_grid,
                         scoring='accuracy',
                         cv=3,
                         verbose=1,
                         random_state=1,
                         n_iter=20)

search.fit(X_train, y_train)

# Best parameters for Random forest classifier
print("Best parameters for Random Forest Classifier : ", search.best_params_)
# Retrain with best model

best_forest = search.best_estimator_

best_forest.fit(X_train, y_train)
print("Best train accuracy for Random Forest Classifier : ", accuracy_score(y_train, best_forest.predict(X_train)))
print("Best test accuracy for Random Forest Classifier : ", accuracy_score(y_test, best_forest.predict(X_test)))
print(classification_report(y_test, best_forest.predict(X_test)))
#---------------------------------------------------------------------------------------------
#Stacking Classifier
stack = StackingClassifier(estimators=[('best tree classifier', best_tree),
                                       ('best logreg', best_logreg),
                                       ('best svc', best_svc),
                                       ('best forest classifier', best_forest)],
                           
                           final_estimator=LogisticRegression(),
                           passthrough=True)

stack.fit(X_train, y_train)

print("Train accuracy : ", accuracy_score(y_train, stack.predict(X_train)))
print("Test accuracy : ", accuracy_score(y_test, stack.predict(X_test)))
print(classification_report(y_test, stack.predict(X_test)))
#---------------------------------------------------------------------------------------------
#Saving the final pipline
# final features
features = ['HAEMATOCRIT', 'HAEMOGLOBINS', 'ERYTHROCYTE', 'LEUCOCYTE','THROMBOCYTE', 'AGE', 'SEX']
num_features = ['HAEMATOCRIT', 'HAEMOGLOBINS', 'ERYTHROCYTE', 'LEUCOCYTE','THROMBOCYTE', 'AGE']

X = data[features] # feature set
y = data['SOURCE'] # target

# Splitting data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)

# Label encoding
X_train.SEX.replace({'M':1, 'F':0}, inplace=True)
X_test.SEX.replace({'M':1, 'F':0}, inplace=True)

# Feature scaling
scaler = MinMaxScaler(feature_range=(0, 1))

X_train[num_features] = scaler.fit_transform(X_train[num_features])
X_test[num_features] = scaler.transform(X_test[num_features])

# Train the final model again!
model = StackingClassifier(estimators=[('best tree classifier', best_tree),
                                       ('best logreg', best_logreg),
                                       ('best svc', best_svc),
                                       ('best forest classifier', best_forest)],
                           
                           final_estimator=LogisticRegression(),
                           passthrough=True)

model.fit(X_train, y_train)
print("Final model trained Successfully!")

# Pickle scaler object
with open("scaler.pkl", 'wb') as file:
    pickle.dump(scaler, file)
    
# Pickle model object
with open("model.pkl", 'wb') as file:
    pickle.dump(model, file)

print("Pickled and Saved Successfully!")


