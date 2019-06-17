import spacy
import os
os.system("python -m spacy download pt")
nlp = spacy.load('pt')

print('ready')
while True:
    text = input()
    doc = nlp(text)
    print('entidades:\n')
    for ent in doc.ents:
        print(ent.text,ent.label_)