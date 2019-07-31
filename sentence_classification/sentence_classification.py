import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
import json
import gzip
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stopwords = set(stopwords.words('english'))
path = 'qa_Appliances.json.gz'

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield eval(l)

def getdata(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma

def get_tokens(sentence):
  tokens = nltk.word_tokenize(sentence)  
  tokens = [token for token in tokens if (token not in stopwords and len(token) > 1)]
  tokens = [get_lemma(token) for token in tokens]
  return (tokens) 

def pre_process_target(y):
  label = preprocessing.LabelEncoder()
  y = label.fit_transform(y)
  return y

def svm_model(X_train,y_train):
    param_grid = [
    {'C': [1, 10], 'kernel': ['linear'], 'verbose':[True]},
    {'C': [1, 10], 'gamma': [0.1,0.01], 'kernel': ['rbf'], 'verbose':[True]},]
    #svm = GridSearchCV(SVC(verbose=True),param_grid)
    svm = SVC(verbose=True)
    svm.fit(X_train, y_train)
    return(svm)

def random_forest_model(X_train, y_train):
  rf = RandomForestClassifier()
  rf.fit(X_train, y_train)
  return rf

'''
token_list = (df['question'].apply(get_tokens))
print(token_list)

yesno = 0
openended =0
for i in (range(len(df))):
  resposta = df['questionType'][i]
  if resposta == 'yes/no':
    yesno += 1
  else:
    openended +=1
'''

df = getdata(path)

token_list = (df['question'].str.lower().apply(get_tokens))
for i in range(len(token_list)):
  token_list[i] = ' '.join(token_list[i])

X = pd.DataFrame(token_list) 

tfidf = TfidfVectorizer()
values = tfidf.fit_transform(X['question'])
feature_names = tfidf.get_feature_names()
X = pd.DataFrame(values.toarray(), columns = feature_names)

y = pre_process_target(df['questionType'])
y = pd.DataFrame(y) 

X_train,X_test, y_train, y_test =  train_test_split(X, y,test_size =0.20,random_state= 4 )


#svm = svm_model(X_train, y_train.values.ravel())
#y_pred = svm.predict(X_test)

rf = random_forest_model(X_train, y_train.values.ravel())
y_pred = rf.predict(X_test)

score = accuracy_score(y_test, y_pred)
print("accuarcy :", score)