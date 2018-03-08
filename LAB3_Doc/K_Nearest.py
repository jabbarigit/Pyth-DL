# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:23:17 2018

@author: Abdoh Jabbari
"""
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split

#in this section we are importing the dataset from sklearn (irisdatasets)
dataset = datasets.load_iris()


 # setting the independent variables 
x=dataset.data
y=dataset.target

# in this line we are splitting the dataset to training and testing sets
# split the data to 25% testing data, 75% training data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25)


# applying K Neighbors Classifier
model= KNeighborsClassifier(n_neighbors=5)
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

print("the accuracy ",metrics.accuracy_score(y_test,y_pred))

#compare the accuracy when K=1 and K is a big number like 50
k_value =range(1,50)
scores=[]

for k in k_value:
    ku=KNeighborsClassifier(n_neighbors=k)
    ku.fit(x_train,y_train)
    y_pred=ku.predict(x_test)
    scores.append(metrics.accuracy_score(y_test,y_pred))

# ploting the results 
import matplotlib.pyplot as plt

plt.plot(k_value,scores)
plt.xlabel("K Values")
plt.ylabel("Accuracy")
plt.show()