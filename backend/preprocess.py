import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove_punc(txt):
    return txt.translate(str.maketrans('','',string.punctuation))  

def remove_num(txt):
    new =""
    for i in txt:
        if not i.isdigit():
            new = new+i
    return new


def remove_emojis(txt):
    new =""
    for i in txt:
        if i.isascii():
            new = new+i
    return new


nltk.download('punkt')
nltk.download('stopwords') 

stop_words = set(stopwords.words('english'))

def remove_fun(txt):
    words = word_tokenize(txt)
    cleaned_txt =[]
    for i in words:
        if not i in stop_words:
            cleaned_txt.append(i)
    return ' '.join(cleaned_txt) 

def preprocess_text(text):
    text = text.lower()
    text = remove_punc(text)
    text = remove_num(text)
    text = remove_emojis(text)
    text = remove_fun(text)
    return text
