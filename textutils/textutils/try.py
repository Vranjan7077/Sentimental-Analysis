# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 20:22:05 2019

@author: Lenovo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('codebeautify.tsv',delimiter='\t',quoting=3)
sarset=pd.read_csv('sarcasam.csv',delimiter='t',quoting=3)
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()

corpus = []
for i in range (0,1995):
    review=dataset['tweets'][i]
    review=re.sub('[^a-zA-z]',' ', review)
    review=review.lower()
    review=review.split()
    review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review=' '.join(review)
    corpus.append(review)
    

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
X=cv.fit_transform(corpus).toarray()
review="i do not hate you"
review=re.sub('[^a-zA-z]',' ', review)
review=review.lower()
review=review.split()

review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
review=' '.join(review)
m=cv.transform([review]).toarray()
Y=dataset.iloc[:,1].values
Y = Y.astype(int)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.10, random_state = 0) 

Y_test=Y_test.astype(int)
Y_train=Y_train.astype(int)
from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(X_train,Y_train)
jkjj

y_pred=classifier.predict(m)
if(y_pred):
    print("sarcastic")
"""else:
    corpus = []
    for i in range (0,17414):
        review=dataset['tweets'][i]
        review=re.sub('[^a-zA-z]',' ', review)
        review=review.lower()
        review=review.split()
        review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
        review=' '.join(review)
        corpus.append(review)
    
    from sklearn.feature_extraction.text import CountVectorizer
    cv=CountVectorizer()
    X=cv.fit_transform(corpus).toarray()
    review="i do not hate you"
    review=re.sub('[^a-zA-z]',' ', review)
    review=review.lower()
    review=review.split()
    p=0
    for i in range (0,len(review)):
        if review[i]=="not":
            p=1
            break
    review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review=' '.join(review)
    m=cv.transform([review]).toarray()
    Y=dataset.iloc[:,1].values
    Y = Y.astype(int)

    from sklearn.model_selection import train_test_split
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.10, random_state = 0) 

    Y_test=Y_test.astype(int)
    Y_train=Y_train.astype(int)
    from sklearn.naive_bayes import GaussianNB
    classifier=GaussianNB()
    classifier.fit(X_train,Y_train)

    y_pred=classifier.predict(m)
    if y_pred==1 and p==1:
        y_pred=0
    elif y_pred==0 and p==1:
        y_pred=1


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(Y_test,y_pred)
"""