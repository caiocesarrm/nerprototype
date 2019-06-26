import spacy
import os
from spacy_ner import ner_controller
import train_data
'''
os.system("python -m spacy download pt")
nlp = spacy.load('pt')

print('ready')
while True:
    text = input()
    doc = nlp(text)
    print('entidades:\n')
    for ent in doc.ents:
        print(ent.text,ent.label_)
'''

#ner = ner_controller(train_data.TRAIN_DATA, 'pt')
#model = ner.create_model()
model = spacy.load("pt")

prep = ['de','da','do']

print('ready')
while True:
    text = input()
    doc = model(text)
    print('entidades:')
    #print(doc.tokens)
    for ent in doc.ents:
        print(ent.text,ent.label_)
    entities = []
    candidates = []
    for token in doc:
        if token.text == 'ou':
            or_index = token.i
    for token in doc:
        print(token.text, token.pos_, token.dep_)
        if token.dep_ == 'ROOT':
            if doc[token.i+2].text in prep:
                candidates.append(doc[token.i+1].text+' '+doc[token.i+2].text+' '+doc[token.i+3].text)
            elif doc[token.i+1].pos_ == 'CCONJ':
                candidates.append(doc[token.i+2].text)
            else:
                candidates.append(doc[token.i+1].text)

        if token.text == 'ou':
            if doc[token.i-2].text in prep:
                candidates.append(doc[token.i-3].text+' '+doc[token.i-2].text+' '+doc[token.i-1].text)
            else:
                candidates.append(doc[token.i+-1].text)
            
            n_words = doc.__len__() - token.i -1
            parts_of_word = []
            for i in range(-n_words, 0):
                #print()
                parts_of_word.append(doc[i].text)
                print(parts_of_word)
            
            candidates.append(' '.join(parts_of_word))
            
    unique_candidates = []
    for i in candidates:
        if i not in unique_candidates:
            unique_candidates.append(i)
    print(unique_candidates)
        

