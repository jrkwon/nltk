#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 21:46:00 2018

@author: jaerock
"""

from nltk.chunk import ne_chunk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

pos = ne_chunk(pos_tag(word_tokenize('My name is Jae Kwon.')))
print(pos)