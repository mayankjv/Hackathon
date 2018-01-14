import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier

data= pd.read_csv('train.csv')
data1=pd.read_csv('test.csv')
X_train =data['title']
y_train = data['category']
X_test =data1['title']
target_names =data1['category']

classifier = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('clf', OneVsRestClassifier(SVC()))])
classifier.fit(X_train, y_train)
predicted = classifier.predict(X_test)
for i in predicted:
	print(i)