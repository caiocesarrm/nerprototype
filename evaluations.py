import spacy
from spacy.gold import GoldParse
from spacy.scorer import Scorer
from spacy_ner import ner_controller
from sklearn.model_selection import KFold
import numpy as np
import train_data_en
import train_data
from spacy_regex import SpacyRegex
from googletrans import Translator

class F_measure:
    def __init__(self):
        self.tp = 0
        self.fp = 0
        self.fn = 0
        self.precision = 0
        self.recall = 0
        self.f1 = 0

    def get_true_entities(self,data):
        phrase = data[0]
        entities = data[1]
        text_entities = []
        for entity in entities.get('entities'):
            text_entities.append(entity)
        true_entities = []
        for entity in text_entities:
            true_entities.append(phrase[entity[0]:entity[1]])
        return true_entities

    def prediction_eval(self, y_true, y_pred):
        for i in y_pred:
            if i in y_true:
                self.tp += 1
            else:
                self.fp += 1
        for i in y_true:
            if i not in y_pred:
                self.fn += 1 
            
        self.f1_score()

    
    def f1_score(self):
        self.precision = self.tp/(self.tp+self.fp)
        self.recall = self.tp/(self.tp+self.fn)
        self.f1 = 2*(self.precision*self.recall)/(self.precision+self.recall)


    def print_stats(self):
        print('False negatives :' + str(self.fn))
        print('True positives :' + str(self.tp))
        print('False positives :' + str(self.fp))
        print('Precision: ' + str(self.precision))
        print('Recall: '+str(self.recall))
        print('F1: ' + str(self.f1))

class SpacyEvaluator:
    train_data = None
    model = None

    def __init__(self, train_data, model):
        self.train_data = train_data
        self.model = model

    def scorer_builtin_spacy(self, nlp, examples, ent='MISC'):
        scorer = Scorer()
        for input_, annot in examples:
            text_entities = []
            for entity in annot.get('entities'):
                if ent in entity:
                    print(ent)
                    text_entities.append(entity)
            doc_gold_text = nlp.make_doc(input_)
            gold = GoldParse(doc_gold_text, entities=text_entities)
            pred_value = nlp(input_)
            scorer.score(pred_value, gold)
        return scorer.scores


    def evaluate_ner(self, n_splits):
        data = self.train_data
        kf = KFold(n_splits=n_splits)
        X = np.array(data)
        scorer = F_measure()
        results = []

        for train_index, test_index in kf.split(X):
            print("TRAIN:", train_index, "TEST:", test_index)
            X_train, X_test = X[train_index], X[test_index]
            ner = ner_controller(data, self.model)
            model = ner.create_model(data=X_train.tolist())
            for data in X_test.tolist():
                doc = model(data[0])
                true_entities = scorer.get_true_entities(data)
                pred_entities = [str(ent) for ent in doc.ents]
                scorer.prediction_eval(true_entities, pred_entities)

            results.append(scorer.f1)
            
        print("Average NER F1 score: " + str(sum(results)/n_splits))
        return results

    def evaluate_regex(self, n_splits):
        model = SpacyRegex(self.model)
        scorer = F_measure()
        kf = KFold(n_splits=n_splits)
        X = np.array(self.train_data)
        results = []
        for train_index, test_index in kf.split(X):
            print("TRAIN:", train_index, "TEST:", test_index)
            X_test = X[test_index]
            for data in X_test.tolist():
                
                true_entities = scorer.get_true_entities(data)
                pred_entities = model.predict(data[0])
                scorer.prediction_eval(true_entities, pred_entities)
            results.append(scorer.f1)

        print("Average Regex F1 score: " + str(sum(results)/n_splits))
        return results

        
        

#evaluator = SpacyEvaluator(train_data_en.TRAIN_DATA, "en_core_web_sm")
#evaluator.evaluate_ner(5)

evaluator = SpacyEvaluator(train_data.TRAIN_DATA, 'pt')
evaluator.evaluate_ner(5)
evaluator.evaluate_regex(5)
'''
from sklearn.metrics import f1_score

y_true = [['teste','teste'], 'vai']
y_pred = ['test', 'vai']

print(f1_score(y_true, y_pred, average='macro'))

phrase = input()
translator = Translator()
translator.translate(phrase, src='pt', dest='en')
    
'''



