# i have created this file -basu13
import os

from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
import pandas as pd
from django.conf import settings
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import re
import nltk
dataset=pd.read_csv(r'C:\Users\ranvi\OneDrive\Desktop\Sentimental-Analysis\textutils\textutils\codebeautify.tsv',delimiter='\t',quoting=3)
sarset=pd.read_csv(r'C:\Users\ranvi\OneDrive\Desktop\Sentimental-Analysis\textutils\textutils\sarcasm.csv',delimiter='\t',quoting=3)
# print(dataset)

nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()


# print(corpus)
"""def sar(request):
    for i in range(0, 7631):
        review = dataset['tweets'][i]
        review = re.sub('[^a-zA-z]', ' ', review)
        review = review.lower()
        review = review.split()
        review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
        review = ' '.join(review)
        corpus.append(review)"""
def index(request):
    return render(request,'article.html')


def rempunc(request):
    text=request.GET.get('text','default')
    punc=request.GET.get('punc','off')
    caps=request.GET.get('caps','off')
    line = request.GET.get('line', 'off')
    space = request.GET.get('space', 'off')
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    res=""
    if(punc=='on'):
        for char in text:
            if char not in punc:
                res = res + char
    elif(caps=='on'):
        for char in text:
                res = res + char.upper()
    elif(line=='on'):
        for char in text:
            if char not in "\n":
                res = res + char
    elif(space=='on'):
        for index,char in enumerate(text):
            if not(text[index]==' ' and text[index+1]==' '):
                res = res + char
    else:
        return HttpResponse("<h1>Error</h1>")
    params={'res': res}
    return render(request,'result.html',params)

from django.conf import settings
from django.core.files.storage import FileSystemStorage

def fileana(request):
    folder='my_folder/'
    if  request.FILES['file1']:
        myfile = request.FILES['file1']
        fs = FileSystemStorage(location=folder) #defaults to   MEDIA_ROOT
        filename = fs.save(myfile.name, myfile)
        file_url = fs.url(filename)
        return render(request, 'article.html')
    else:
         return render(request, 'article.html')
global z
z=0
def upload(request):
    #  Saving POST'ed file to storage
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    #  Reading file from storage
    #file = default_storage.open(file_name)
    #file_url = default_storage.url(file_name)
    from shutil import copyfile
    dst = 'C:/Users/Singhai/Desktop/positive/'
    pst = 'C:/Users/Singhai/Desktop/negative/'
    path = 'C:/Users/Singhai/Desktop'
    import glob
    for filename in glob.glob(os.path.join(path, '*.txt')):
        src = filename
        k = open(filename, "r")
        p = k.readlines()
        k.close()
    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer()
    X = cv.fit_transform(corpus).toarray()
    review = k
    review = re.sub('[^a-zA-z]', ' ', review)
    review = review.lower()
    review = review.split()
    p = 0
    for i in range(0, len(review)):
        if review[i] == "not":
            p = 1
            break
    review = [ps.stem(word) for womjrd in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    m = cv.transform([review]).toarray()
    Y = dataset.iloc[:, 1].values
    Y = Y.astype(int)

    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.10, random_state=0)

    Y_test = Y_test.astype(int)
    Y_train = Y_train.astype(int)
    from sklearn.naive_bayes import GaussianNB
    classifier = GaussianNB()
    classifier.fit(X_train, Y_train)

    y_pred = classifier.predict(m)
    if y_pred == 1 and p == 1:
        y_pred = 0
    elif y_pred == 0 and p == 1:
        y_pred = 1

    # from sklearn.metrics import confusion_matrix
    # cm = confusion_matrix(Y_test, y_pred)

    res = ""
    if (y_pred == 0):
        res = "Negative"
    elif (y_pred == 1 and  z==1):
        res = "2"
    else:
        res="1"
    # dataset.drop()
    # corpus.clear()
    params = {'res': res}
    return render(request, 'article.html', params)
serpus = []
for i in range(0, 1994):
    review = sarset['tweets'][i]
    review = re.sub('[^a-zA-z]', ' ', review)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    serpus.append(review)
from sklearn.naive_bayes import GaussianNB
def sar(request):
    k = request.GET.get('text', 'default')
    cv = CountVectorizer()
    X = cv.fit_transform(serpus).toarray()
    review = k
    review = re.sub('[^a-zA-z]', ' ', review)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    m = cv.transform([review]).toarray()
    Y = sarset.iloc[:, 1].values
    Y = Y.astype(int)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.10, random_state=0)
    Y_test = Y_test.astype(int)
    Y_train = Y_train.astype(int)
    classifier = GaussianNB()
    classifier.fit(X_train, Y_train)
    y_pred = classifier.predict(m)
    # from sklearn.metrics import confusion_matrix
    # cm = confusion_matrix(Y_test, y_pred)
    res=""
    global z
    z=y_pred
    return article(request)


corpus = []
for i in range(0, 7631):
    #load data
    review = dataset['tweets'][i]
    review = re.sub('[^a-zA-z]', ' ', review)
    review = review.lower()
    #print(review)

    review = review.split()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

def article(request):
    k = request.GET.get('text', 'default')
    cv = CountVectorizer()
    X = cv.fit_transform(corpus).toarray()
    review = k
    review = re.sub('[^a-zA-z]', ' ', review)
    review = review.lower()

    # Tokenize
    review = review.split()
    #print(review)

    p = 0
    for i in range(0, len(review)):
        if review[i] == "not":
            p = 1
            break

    # stemming  and stopwords
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    print(review)


    m = cv.transform([review]).toarray()
    Y = dataset.iloc[:, 1].values
    Y = Y.astype(int)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.10, random_state=0)
    Y_test = Y_test.astype(int)
    Y_train = Y_train.astype(int)
    classifier = GaussianNB()
    classifier.fit(X_train, Y_train)
    y_pred = classifier.predict(m)
    if y_pred == 1 and p == 1:
        y_pred = 0
    elif y_pred == 0 and p == 1:
        y_pred = 1

    # from sklearn.metrics import confusion_matrix
    # cm = confusion_matrix(Y_test, y_pred)

    res=""
    if(y_pred==0):
        res="0"
    elif(y_pred==1 and z==1):
        res="2"
    else:
        res="1"
    # dataset.drop()
    # corpus.clear()
    params={'res':res}
    return render(request,'article.html',params)
