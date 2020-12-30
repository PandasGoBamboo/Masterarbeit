import json, csv, pandas as pd 
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, make_scorer, classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression, SGDClassifier, LogisticRegressionCV
from sklearn.preprocessing import StandardScaler, Binarizer
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score, cross_val_predict, GridSearchCV
from nltk.corpus import stopwords
from sklearn.svm import SVC
from stoppwords_german import german_stop_words 

############################ Datei laden

path = 'path/to/file/'
all = pd.read_csv(path + 'file.csv', encoding='utf-8', sep=';')

# Trainingsklassen aus Spalte "brand" der CSV-Datei
y = all['brand']
# Trainingsdaten aus der Spalte "stemmed" der CSV-Datei. Enthält die Textdaten
X = all['stemmed']

############################ Cross-Validation mit Vektorisierung, Klassifikation und Parametertuning

##### Initialisierung des KFold
# n_split =   Anzahl, wie oft Daten aufgeteilt werden
# shuffle =   Randomisiert die Daten. Da sie in der Datei nach Klassen sortiert sind,
#             muss dieser Param gesetzt werden.
# rnd_state = Eine beliebige Zahl. Dadurch wird gesichert, dass immer dieselbe Aufteilung 
#             erfolgt. 
kf = KFold(n_splits=10, shuffle=True, random_state=42)

# Vektorisierungsmethode 
vectorizier = CountVectorizer()
# tfidf = TfidfTransformer()

# Klassifikator
classifier = SGDClassifier()
scaler = StandardScaler()

pipe = Pipeline([
    ('vect', vectorizier),
    ('tfidf', tfidf),
    ('scaler', scaler),
    ('svm', classifier)
    ])

params = {
    "vect__lowercase": [False],
    "vect__stop_words": [german_stop_words],
    "scaler__with_mean": [False],
    "svm__alpha": [0.01]
    }

clf = GridSearchCV(pipe, param_grid = params, cv = kf )

# Auskommentieren für Anzeige der besten Parameter
#clf.fit(X, y)
#print(clf.best_params_)

# Ausgabe der Ergebnisse
y_pred = cross_val_predict(clf, X, y)
print(classification_report(y, y_pred))

