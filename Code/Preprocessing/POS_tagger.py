import pickle
from ClassifierBasedGermanTagger.ClassifierBasedGermanTagger import ClassifierBasedGermanTagger
from germalemma import GermaLemma
import nltk
from nltk import pos_tag, sent_tokenize, word_tokenize
from nltk.stem import SnowballStemmer
import json, csv, pandas as pd 
import glob
import numpy as np

# Trainerter Korpus aus ClassiferBasedGermanTagger.py
with open('Pfad/zu/trainierten/Korpus/aus/ClassiferBasedGermanTagger.py', 'rb') as f:
    tagger = pickle.load(f)

# CSV-Datei deren Wörter getaggt werden sollen
in_path = 'pfad/zu/ordner/'
filename = 'filename.csv'

data = pd.read_csv(in_path + filename + '.csv', sep=';', encoding='utf-8')

# Spalte mit den zu  taggenden Texten
text = data['text']

# Funktion zum POS-Tagging
def TagPOS_Text(text_list):
    pos_list = []
    for row in text_list:
        new_row = row.split(' ')
        tagged_sent = tagger.tag(new_row)
        pos_list.append(tagged_sent)
    return pos_list

pos = TagPOS_Text(text)