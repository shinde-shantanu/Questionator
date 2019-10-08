# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 09:14:31 2019

@author: naeem
"""

import nltk

from nltk.corpus import wordnet


synonyms=[]
antonyms=[]

for syn in wordnet.synsets("cricketer"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
            
print(set(synonyms))
print(set(antonyms))