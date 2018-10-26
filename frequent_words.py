#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 20:54:00 2018

@author: shufakhizra
"""

import pandas as pd
from nltk.corpus import stopwords
import re


global frequent_words
frequent_words = {}


def emoji_tweets(x, emojis):
    global frequent_words
    flag =0
    y = x.split()
    for i in y:
        for k in emojis:
            if i == k:
                flag = 1
    if flag==1:
        for i in y:
            if re.search(r"^([a-z])", i) and i!= 'user':
                frequent_words[i] = 0
        #print("hello", x)
        return x
    else:
        return float('NaN')


def count_frequent_words(x):
    global frequent_words
    y = x.split()
    for i in y:
        for j in frequent_words:
            if i == j:
                frequent_words[i] = frequent_words[i] + 1


    
#emojis = [':fire:', ':heavy_check_mark:', ':rocket:']
#emojis = [':green_heart:']

#emojis = [':face_with_tears_of_joy:']
#emojis = [':loudly_crying_face:']
#emojis = [':crying_face:']

emojis = [':fire:']
#emojis = [':smiling_face_with_heart-eyes:']

#data = pd.DataFrame.from_csv('processed_text_eagles_before.csv', encoding='utf-8', index_col= None)
#data = pd.DataFrame.from_csv('processed_text_patriots_before.csv', encoding='utf-8', index_col= None)
#data = pd.DataFrame.from_csv('processed_text_superbowl_before.csv', encoding='utf-8', index_col= None)



#data = pd.DataFrame.from_csv('processed_text_eagles_after.csv', encoding='utf-8', index_col= None)
data = pd.DataFrame.from_csv('processed_text_patriots_after.csv', encoding='utf-8', index_col= None)
#data = pd.DataFrame.from_csv('processed_text_superbowl_after.csv', encoding='utf-8', index_col= None)


#data = pd.DataFrame.from_csv('processed_text_eagles.csv', encoding='utf-8', index_col= None)
#data = pd.DataFrame.from_csv('processed_text_patriots.csv', encoding='utf-8', index_col= None)
#data = pd.DataFrame.from_csv('processed_text_superbowl.csv', encoding='utf-8', index_col= None)



#data = pd.DataFrame.from_csv('processed_text_bitcoin.csv', encoding='utf-8', index_col= None)
#data = pd.DataFrame.from_csv('pre_text_bitcoin.csv', encoding='utf-8', index_col= None)


data.text = data.text.astype(str)


#remove stop words
stop = stopwords.words('english')
data['text'] = data['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))

#df = pd.DataFrame(columns=["text"])
#print(data.text)

data.text = data.text.apply(lambda x: emoji_tweets(x, emojis))

data.dropna(subset=['text'], how='all', inplace = True)

print(len(data))
data.text = data.text.apply(lambda x: count_frequent_words(x))

from collections import Counter
frequent_words = dict(Counter(frequent_words).most_common(40))

print(frequent_words)



