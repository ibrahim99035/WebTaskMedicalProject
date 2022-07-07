import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
dataSet = pd.read_csv('heart.csv')
dataSet.head(30)
dataSet.describe()
dataSet['target'].value_counts()
dataSet.groupby('target').mean()
df_copy =dataSet.copy(deep=True)
df_copy[['age' , 'sex' , 'cp' , 'trestbps' , 'chol' , 'fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','target']] = df_copy[['age' , 'sex' , 'cp' , 'trestbps' , 'chol' , 'fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','target']].replace(0 , np.NaN)
df_copy['age'].fillna(df_copy['age'].mean() , inplace = True)
df_copy['sex'].fillna(df_copy['sex'].mean() , inplace = True)
df_copy['cp'].fillna(df_copy['cp'].mean() ,  inplace = True)
df_copy['trestbps'].fillna(df_copy['trestbps'].mean() ,  inplace = True)
df_copy['chol'].fillna(df_copy['chol'].mean() ,  inplace = True)
df_copy['fbs'].fillna(df_copy['fbs'].mean() ,  inplace = True)
df_copy['restecg'].fillna(df_copy['restecg'].mean() ,  inplace = True)
df_copy['thalach'].fillna(df_copy['thalach'].mean() ,  inplace = True)
df_copy['exang'].fillna(df_copy['exang'].mean() ,  inplace = True)
df_copy['oldpeak'].fillna(df_copy['oldpeak'].mean() ,  inplace = True)
df_copy['slope'].fillna(df_copy['slope'].mean() ,  inplace = True)
df_copy['ca'].fillna(df_copy['ca'].mean() ,  inplace = True)
df_copy['thal'].fillna(df_copy['thal'].mean() ,  inplace = True)
#df_copy['target'].fillna(df_copy['target'].mean() ,  inplace = True)
#from sklearn.model_selection import train_test_split
x = dataSet.drop(columns = 'target',axis = 1)
y = dataSet['target']
scalar = StandardScaler()
scalar.fit(x)
standarized_data = scalar.transform(x)
x = standarized_data
y = dataSet['target']
x_train , x_test , y_train , y_test = train_test_split(x ,y , test_size =0.2 ,stratify=y,random_state=2)
print(x.shape,x_train.shape,x_test.shape)
from sklearn.ensemble import RandomForestClassifier
Classifier = RandomForestClassifier(n_estimators =20)
Classifier.fit(x_train , y_train)
x_train_prediction = Classifier.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction,y_train)
print(f'The Accuracy of training : {training_data_accuracy}')
x_test_prediction = Classifier.predict(x_test)
test_data_accuracy = accuracy_score(x_test_prediction,y_test)
print(f'The Accuracy of test : {test_data_accuracy}')
instance = (70,1,0,145,174,0,1,125,1,2.6,0,0,3)
arr = np.asarray(instance)
reshape = arr.reshape(1,-1)
std = scalar.transform(reshape)
prediction = Classifier.predict(std)
if(prediction[0]==0):
    print('Not Heart')
else :
    print('Heart')
    
#filename = 'heart.pdl'
#pickle.dump(classifier , open(filename ,'wb'))

