#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 23:32:25 2018

@author: jaerock
"""

from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hello Mr. Smith, how are you today? The weather is great and Python is awesome. The sky is pinkish-blue. You should not eat cardboard."

print(sent_tokenize(example_text))

print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)
    
    
    
    