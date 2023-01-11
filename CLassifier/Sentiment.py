import numpy as np
import string
import pandas as pd
import re
import pickle

import warnings
warnings.filterwarnings("ignore")

tfidf = pickle.load(open('tfidf.pkl', 'rb'))

lr = pickle.load(open('lrmodel.pkl', 'rb'))

stopwordlist = pd.read_csv('stopwords.dat', header=None)[0].values

STOPWORDS = set(stopwordlist)

def cleaning_quots(text):
    return re.sub('&quot;', '', text).strip()

def cleaning_URLs(text):
    cll = re.sub('http\S+','',text)
    cll = re.sub('www\S+','',cll)
    return cll

def get_decontracted(phrase):
    phrase = str.lower(phrase)
    
    # specific
    phrase = re.sub(r"won\'t", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)
    phrase = re.sub(r"ain\'t", "am not", phrase)
    phrase = re.sub(r"gonna","going to", phrase)
    phrase = re.sub(r"wanna","want to", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase

def cleaning_weird_char(text):
    return ''.join(e for e in text if e in string.ascii_letters+' ')

def cleaning_doublespaces(text):
    return re.sub('  ',' ',text).strip()

def cleaning_stopwords(text):
    return " ".join([word for word in text.split() if word not in STOPWORDS])

def cleaning_repeating_char(text):
    return re.sub(r'(.)\1+', r'\1', text)

def preprocess(text):
    inp = cleaning_quots(text)
    inp = cleaning_URLs(inp)
    inp = get_decontracted(inp)
    inp = cleaning_weird_char(inp)
    inp = cleaning_doublespaces(inp)
    inp = cleaning_stopwords(inp)
    inp = cleaning_repeating_char(inp)
    return inp

def predict_sentiment(text):
    
    vec = tfidf.transform(pd.Series([text]))
    
    y_pred = lr.predict(vec)
    
    if(y_pred[0]>0.5): print('\nPositive\n')
    else: print('\nNegative\n')


def main():
    text = input('Please enter your tweet!\n')
#     warnings.filterwarnings("ignore")
    
    while(text!='exit!'):
        inp = preprocess(text)
        
        if((inp == '') or(inp==' ')): print('No processable input given\n')
        else: predict_sentiment(inp)
        
        text = input('Try another one!\n')
        
main()

        




