import spacy
from spacy.gold import GoldParse
from spacy.scorer import Scorer
from spacy_ner import ner_controller
from sklearn.model_selection import KFold
import numpy as np
import train_data

class SpacyNerEvaluator:

    def score_spacy(self, nlp, examples, ent='MISC'):
        scorer = Scorer()
        for input_, annot in examples:
            text_entities = []
            for entity in annot.get('entities'):
                if ent in entity:
                    text_entities.append(entity)
            doc_gold_text = nlp.make_doc(input_)
            gold = GoldParse(doc_gold_text, entities=text_entities)
            pred_value = nlp(input_)
            scorer.score(pred_value, gold)
        return scorer.scores


    def evaluate(self, n_splits, data):
        kf = KFold(n_splits=n_splits)
        X = np.array(data)
        results = []

        for train_index, test_index in kf.split(X):
            print("TRAIN:", train_index, "TEST:", test_index)
            X_train, X_test = X[train_index], X[test_index]
            ner = ner_controller()
            model = ner.create_model(data=X_train.tolist())
            results.append(self.score_spacy(model, X_test.tolist()))
        
        for i in results:
            print(i)
        return results


evaluator = SpacyNerEvaluator()
evaluator.evaluate(5, train_data.TRAIN_DATA)



    




