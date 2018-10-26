#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 23:39:36 2018

@author: shufakhizra
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 22:49:56 2018

@author: shufakhizra
"""
import pandas as pd
from textblob import TextBlob
from nltk.corpus import stopwords
import re


data = pd.DataFrame.from_csv('processed_text_bitcoin.csv', encoding='utf-8', index_col= None)

#data = pd.DataFrame.from_csv('pre_text_bitcoin.csv', encoding='utf-8', index_col= None)

data.text = data.text.astype(str)

pos =0
neg =0
neu =0


def emoji_tweets(x):
    flag =0
    y = x.split()
    for i in y:
        if re.search(r"^(:)", i):
                flag = 1
    if flag==1:
        return x
    else:
        return float('NaN')



def polarity_count(x):
    global pos
    global neg
    global neu
    value =0
    blob = TextBlob(x)
    for sentence in blob.sentences:
        value = sentence.sentiment.polarity
    if value >0.2:
        pos = pos + 1
        print(x)
    else: 
        if value <0.2:
            neg = neg + 1
        else:
            neu = neu + 1

'''    
#removing stop words    
stop = stopwords.words('english')
data['text'] = data['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
data.dropna(subset=['text'], how='all', inplace = True)
'''
#print(data.text)    

data.text = data.text.apply(lambda x: emoji_tweets(x))
data.dropna(subset=['text'], how='all', inplace = True)



data.text.apply(lambda x: polarity_count(x))

print("positive:", pos)
print("negative:" , neg)
print("neutral:" , neu)
    

'''
stop = stopwords.words('english')
data['text'] = data['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
'''

  
