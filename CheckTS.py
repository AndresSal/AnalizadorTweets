import sys
import textblob
import re
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from textblob.classifiers import NLTKClassifier

with open('trainningUno1.csv', 'r') as fp:
    cl = NaiveBayesClassifier(fp,format="csv")


print(cl.classify("Siempre te inventas respuestas para todo MAMARRACHO INSULTADOR DE MUJERES"))

with open('test.csv', 'r') as ft:
    print(cl.accuracy(ft,format="csv"))