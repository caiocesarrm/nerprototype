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
                random.shuffle(data)
                batches = minibatch(data, size=sizes)
                losses = {}
                for batch in batches:
                    texts, annotations = zip(*batch)
                    nlp.update(texts, annotations, sgd=optimizer, drop=0.35, losses=losses)
        return nlp

    def create_model(self, data=None, labels=None):
        if data is None:
            data = self.TRAIN_DATA
        if labels is None:
            labels = self.NEW_LABELS

        model = self.train_model(data, labels)
        return model


