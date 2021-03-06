#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 23:41:11 2018

@author: jaerock
"""

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))

print(lemmatizer.lemmatize("better", pos="a")) # adj
print(lemmatizer.lemmatize("best", pos="a"))
print(lemmatizer.lemmatize("run", 'v'))

