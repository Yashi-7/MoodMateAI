import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer 
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from preprocess import preprocess_text
from sklearn.metrics import classification_report


df=pd.read_csv("train.txt",sep=';',header=None,names=['text','emotion']) 

uni_emo = df['emotion'].unique()
emo_no ={}
i=0
for e in uni_emo:
    emo_no[e]=i
    i +=1
  

df['emotion'] = df['emotion'].map(emo_no)   
df['text'] = df['text'].apply(lambda x : x.lower())
 
df['text'] = df['text'].apply(preprocess_text)


X_train, X_test, y_train, y_test = train_test_split(df['text'], df['emotion'], test_size=0.20, random_state=42)  

bow_vec = CountVectorizer() 

X_train_bow = bow_vec.fit_transform(X_train)
X_test_bow = bow_vec.transform(X_test) 

nb_model = MultinomialNB() 
nb_model.fit(X_train_bow,y_train)
pred_nb = nb_model.predict(X_test_bow) 
print(accuracy_score(y_test,pred_nb))  

  
tfidf_vec = TfidfVectorizer(
    ngram_range=(1,2)
)
X_train_tfidf = tfidf_vec.fit_transform(X_train)
X_test_tfidf = tfidf_vec.transform(X_test
                                   ) 
nb2_model = MultinomialNB()

nb2_model.fit(X_train_tfidf,y_train)

y_pred = nb2_model.predict(X_test_tfidf)  

print(accuracy_score(y_test,y_pred)) 

lm = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)

lm.fit(X_train_tfidf,y_train) 
y_pr = lm.predict(X_test_tfidf) 
print(accuracy_score(y_test,y_pr)) 
print(classification_report(y_test, y_pr))

import pickle

pickle.dump(lm, open("model.pkl", "wb"))
pickle.dump(tfidf_vec, open("vectorizer.pkl", "wb"))

print("Model and vectorizer saved successfully!")