from django.http import HttpResponse
from django.shortcuts import render

def demo(request):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    dataset = pd.read_csv('codebeautify.tsv', delimiter='\t', quoting=3)
    # print(dataset)
    import re
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    ps = PorterStemmer()
    corpus = []
    for i in range(0, 7631):
        review = dataset['tweets'][i]
        review = re.sub('[^a-zA-z]', ' ', review)
        review = review.lower()
        review = review.split()
        review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
        review = ' '.join(review)
        corpus.append(review)
    # print(corpus)

    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer()
    X = cv.fit_transform(corpus).toarray()
    k = request.GET.get('data','default')
    m = cv.transform([k]).toarray()
    Y = dataset.iloc[:, 1].values
    Y = Y.astype(int)
    # print(X)
    # print(Y)
    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.10, random_state=0)
    # print(X_train)
    Y_test = Y_test.astype(int)
    Y_train = Y_train.astype(int)
    from sklearn.naive_bayes import GaussianNB
    classifier = GaussianNB()
    classifier.fit(X_train, Y_train)

    y_pred = classifier.predict(m)

    # from sklearn.metrics import confusion_matrix
    # cm=confusion_matrix(Y_test,y_pred)
    res=""
    if(y_pred==0):
        res="Negative"
    else:
        res="Positive"
    params={'res':res}
    return render(request,'demo.html',params)

