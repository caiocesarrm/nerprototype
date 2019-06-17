import spacy
import os
import train_data
os.system("python -m spacy download pt")
import random
from spacy.util import minibatch, compounding

class ner_controller:
    NEW_LABELS = ['MISC']
    TRAIN_DATA = train_data.TRAIN_DATA
    
    def train_model(self, data, labels, iterations=20, model='pt'):
        """Set up the pipeline and entity recognizer, and train the new entity."""
        random.seed(0)
        if model is not None:
            nlp = spacy.load(model)  # load existing spaCy model
        else:
            nlp = spacy.blank(model)  # create blank Language class
            
        if "ner" not in nlp.pipe_names:
            ner = nlp.create_pipe("ner")
            nlp.add_pipe(ner)
            
        else:
            ner = nlp.get_pipe("ner")
        
        for label in labels:
            ner.add_label(label)
        
        optimizer = nlp.begin_training()
        
        move_names = list(ner.move_names)
        
        other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
        with nlp.disable_pipes(*other_pipes):  # only train NER
            sizes = compounding(1.0, 4.0, 1.001)
            
            for itn in range(iterations):
                random.shuffle(self.TRAIN_DATA)
                batches = minibatch(self.TRAIN_DATA, size=sizes)
                losses = {}
                for batch in batches:
                    texts, annotations = zip(*batch)
                    nlp.update(texts, annotations, sgd=optimizer, drop=0.35, losses=losses)
        return nlp

    def create_model(self):
        model = self.train_model(self.TRAIN_DATA, self.NEW_LABELS)
        return model

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

'''