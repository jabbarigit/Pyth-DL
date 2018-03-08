# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:23:17 2018

@author: Abdoh Jabbari
"""
# lists of libraries that are we need to this code 
from sklearn import svm, datasets,metrics
from sklearn.model_selection import train_test_split

dig = datasets.load_digits()
x=dig.data
y=dig.target

# in this line we are splitting the dataset to training and testing sets
# split the data to 20% testing data, 80% training data

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, random_state = 0)

# applying linear kernel model
Lmode = svm.SVC(kernel='linear', C=2, gamma=2)

#Fit trening and testing sets into the model 
Lmode.fit(x_train,y_train)
y_pred=Lmode.predict(x_test)


print ('The Kernal linear accuracy is: ',metrics.accuracy_score(y_test,y_pred))


#applying rbf kernel 
Rmode =svm.SVC(kernel='rbf',C=2, gamma=2)


#Fit trening and testing sets into the model 
Rmode.fit(x_train,y_train)
y_pred=Rmode.predict(x_test)


print ('The kernel rbf accuracy is: ',metrics.accuracy_score(y_test,y_pred))