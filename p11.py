#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 23:09:37 2018

@author: jaerock
"""

import nltk
import random
from nltk.corpus import movie_reviews

# in each category (pos or neg)
# take all the file ids, 
# then, store thw word_tokenzed version for the filed id, 
# followed by pos or neg label 
# in a big list
documents = [(list(movie_reviews.words(fileid)), category)
            for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)]

# shuffle - this is important to train
random.shuffle(documents)
print(documents)

# collect all words
all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

# to find out the most commo words
all_words = nltk.FreqDist(all_words)

# print out the 15 most common words
print(all_words.most_common(15))

# print how many occurrences "stupid"
print(all_words["stupid"])