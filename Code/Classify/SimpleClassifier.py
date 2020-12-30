import json, csv, pandas as pd 
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression, SGDClassifier, LogisticRegressionCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, cross_val_predict, GridSearchCV, KFold, ShuffleSplit
from stoppwords_german import german_stop_words 

# Einfache Klassifikation ohne jegliche Parametereinstellung oder Cross-Validierung

############################ Datei laden
path = 'path/to/file/'
all = pd.read_csv(path + 'file.csv', encoding='utf-8', sep=';')

# Trainingsklassen aus Spalte "brand" der CSV-Datei
y = all['brand']
# Trainingsdaten aus der Spalte "stemmed" der CSV-Datei. Enthält die Textdaten
X = all['stemmed']


# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

############################ Vektorisierung
cv = CountVectorizer()
cv.fit(X_train)

X_train = cv.transform(X_train)
X_test = cv.transform(X_test)

############################ Klassifikation


# Logistische Regression
clf = LogisticRegression(max_iter=500)
scaler = StandardScaler(with_mean=False)
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

"""
# Naiver Bayes

mNB = MultinomialNB()
mNB.fit(X_train, y_train)
y_pred = mNB.predict(X_test)

# Support Vektor Maschine

svm = SGDClassifier()
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)

"""

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print('accuracy %s' % accuracy_score(y_pred, y_test))
print(classification_report(y_test, y_pred))