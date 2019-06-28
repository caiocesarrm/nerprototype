import spacy
import os
import numpy as np

class SpacyRegex:
    def __init__(self, model=None):
        if model is None:
            self.model = spacy.load("pt")
        else:
            self.model = spacy.load(model)


    def after_root_candidates(self, candidates, root_dist, token, doc, prep):
        if doc[token.i+root_dist + 2].text in prep:
            if doc[token.i+root_dist +3].text == 'ou':
                candidates.append(doc[token.i+root_dist +1].text+' '+doc[token.i+root_dist +2].text)
            else:
                candidates.append(doc[token.i+root_dist +1].text+' '+doc[token.i+root_dist +2].text+' '+doc[token.i+root_dist +3].text)
        elif doc[token.i+1].pos_ == 'CCONJ':
            candidates.append(doc[token.i+root_dist +2].text)
        else:
            candidates.append(doc[token.i+root_dist +1].text)

    def predict(self, text):
        prep = ['de','da','do', 'com']
        forbidden_words = prep + ['ou']
        doc = self.model(text)
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
                    self.after_root_candidates(candidates, 1, token, doc, prep)
                else:
                    self.after_root_candidates(candidates, 0, token, doc, prep)

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
