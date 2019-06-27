import spacy
import os
from spacy_ner import ner_controller
import train_data
from spacy_ner import ner_controller
from sklearn.model_selection import KFold
import numpy as np

def get_true_entities(data):
    phrase = data[0]
    entities = data[1]
    text_entities = []
    for entity in entities.get('entities'):
        text_entities.append(entity)
    true_entities = []
    for entity in text_entities:
        true_entities.append(phrase[entity[0]:entity[1]])
    return true_entities

def after_root_candidates(candidates, root_dist, token, doc, prep):
    if doc[token.i+root_dist + 2].text in prep:
        if doc[token.i+root_dist +3].text == 'ou':
            candidates.append(doc[token.i+root_dist +1].text+' '+doc[token.i+root_dist +2].text)
        else:
            candidates.append(doc[token.i+root_dist +1].text+' '+doc[token.i+root_dist +2].text+' '+doc[token.i+root_dist +3].text)
    elif doc[token.i+1].pos_ == 'CCONJ':
        candidates.append(doc[token.i+root_dist +2].text)
    else:
        candidates.append(doc[token.i+root_dist +1].text)

def regex_predict(text, model):
    prep = ['de','da','do', 'com']
    forbidden_words = prep + ['ou']
    doc = model(text)
    entities = []
    candidates = []
    or_index = doc.__len__()
    root_index = -1
    for token in doc:
        if token.text == 'ou':
            or_index = token.i
        if token.dep_ == 'ROOT':
            root_index = token.i
    
    options = []
    for i in range(root_index + 1, or_index):
        options.append(doc[i].text)
    options.append(' '.join(options))
    options = options[-1]


    for token in doc:
        #print(token.text, token.pos_, token.dep_)
        if token.dep_ == 'ROOT':
            if doc[token.i+1].dep_ == 'xcomp' and doc[token.i+2].pos_ != 'VERB':
                after_root_candidates(candidates, 1, token, doc, prep)
            else:
                after_root_candidates(candidates, 0, token, doc, prep)

        if token.text == 'ou':
            if doc[token.i-2].text in prep:
                candidates.append(doc[token.i-3].text+' '+doc[token.i-2].text+' '+doc[token.i-1].text)
            elif doc[token.i-1].text in prep:
                preposition = doc[token.i-1].text
                complement = doc[-1].text
                full_answer = ' '.join((preposition, complement))
                candidates.append(full_answer)
            else:
                candidates.append(doc[token.i-1].text)

            n_words = doc.__len__() - token.i -1
            parts_of_word = []
            for i in range(-n_words, 0):
                parts_of_word.append(doc[i].text)
            
            candidates.append(' '.join(parts_of_word))
    
    unique_candidates = []
    for i in candidates:
        if i not in unique_candidates:
            if i not in forbidden_words:
                unique_candidates.append(i)
    return unique_candidates

def prediction_eval(y_true, y_pred, tp, fp, fn):
    for i in y_pred:
        if i in y_true:
            tp += 1
        else:
            fp += 1
    for i in y_true:
        if i not in y_pred:
            fn += 1 

    return tp, fp, fn
    
def f1_score(tp, fp, fn):
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1 = 2*(precision*recall)/(precision+recall)

    print('False negatives :' + str(fn))
    print('True positives :' + str(tp))
    print('False positives :' + str(fp))
    print('Precision: ' + str(precision))
    print('Recall: '+str(recall))
    print('F1: ' + str(f1))
    return f1


model = spacy.load("pt")
print('ready')
tp = 0
fp = 0
fn = 0
'''

for data in train_data.TRAIN_DATA:
    print(data[0])
    true_entities = get_true_entities(data)
    pred_entities = regex_predict(data[0], model)
    print(true_entities)
    print(pred_entities)

    tp, fp, fn = prediction_eval(true_entities, pred_entities, tp, fp, fn)
    #a = input()
f1_score(tp, fp, fn)

'''
data = train_data.TRAIN_DATA
kf = KFold(n_splits=5)
X = np.array(data)
results = []
f1 = 0
for train_index, test_index in kf.split(X):
    tp = 0
    fp = 0
    fn = 0
    
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    for data in X_test.tolist():
        
        true_entities = get_true_entities(data)
        pred_entities = regex_predict(data[0], model)
        #print(data[0])
        #print(true_entities)
        #print(pred_entities)

        tp, fp, fn = prediction_eval(true_entities, pred_entities, tp, fp, fn)
        #a = input()
    f1 += f1_score(tp, fp, fn)

f1 = f1/5
print("F1 MEDIO: " + str(f1))
'''
data = train_data.TRAIN_DATA
kf = KFold(n_splits=5)
X = np.array(data)
results = []

for train_index, test_index in kf.split(X):
    tp = 0
    fp = 0
    fn = 0
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    ner = ner_controller(data, 'pt')
    model = ner.create_model(data=X_train.tolist())
    
    for data in X_test.tolist():
        doc = model(data[0])
        pred_entities = [str(ent) for ent in doc.ents]
        true_entities = get_true_entities(data)
        tp, fp, fn = prediction_eval(true_entities, pred_entities, tp, fp, fn)
    
    f1_score(tp, fp, fn)
    
    
'''

