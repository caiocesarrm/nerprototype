import spacy
import os
from spacy_ner import ner_controller
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

ner = ner_controller()
model = ner.create_model()

print('ready')
while True:
    text = input()
    doc = model(text)
    print('entidades:')
    for ent in doc.ents:
        print(ent.text,ent.label_)
    #for token in doc:
    #    print(token.text, token.pos_, token.dep_)
