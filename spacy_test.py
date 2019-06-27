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
def after_root_candidates(candidates, root_dist, token, doc):
    if doc[token.i+root_dist + 2].text in prep:
        if doc[token.i+root_dist +3].text == 'ou':
            candidates.append(doc[token.i+root_dist +1].text+' '+doc[token.i+root_dist +2].text)
        else:
            candidates.append(doc[token.i+root_dist +1].text+' '+doc[token.i+root_dist +2].text+' '+doc[token.i+root_dist +3].text)
    elif doc[token.i+1].pos_ == 'CCONJ':
        candidates.append(doc[token.i+root_dist +2].text)
    else:
        candidates.append(doc[token.i+root_dist +1].text)


#ner = ner_controller(train_data.TRAIN_DATA, 'pt')
#model = ner.create_model()
model = spacy.load("pt")

prep = ['de','da','do', 'com']
forbidden_words = prep + ['ou']

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
        print(token.text, token.pos_, token.dep_)
        if token.dep_ == 'ROOT':
            if doc[token.i+1].dep_ == 'xcomp' and doc[token.i+2].pos_ != 'VERB':
                after_root_candidates(candidates, 1, token, doc)
            else:
                after_root_candidates(candidates, 0, token, doc)

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
    
    print(candidates)
    unique_candidates = []
    for i in candidates:
        if i not in unique_candidates:
            if i not in forbidden_words:
                unique_candidates.append(i)
    print(unique_candidates)
        

