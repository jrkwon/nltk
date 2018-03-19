#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 23:48:08 2018

@author: jaerock
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example showing off stop word filtration."
#stop_words = set(stopwords.words("english"))
stop_words = stopwords.words("english")

words = word_tokenize(example_sentence)

#filtered_sentence = []
#
#for w in words:
#    if w not in stop_words:
#        filtered_sentence.append(w)

#filtered_sentence = [w for w in words if not w in stop_words]
filtered_sentence = [w for w in words if w not in stop_words]
        
print(words)
print(filtered_sentence)