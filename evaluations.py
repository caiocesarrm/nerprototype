import spacy
from spacy.gold import GoldParse
from spacy.scorer import Scorer
from spacy_ner import ner_controller

def evaluate(nlp, examples, ent='MISC'):
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


examples = [
    ('você prefere android ou ios', {'entities': [(13, 20, 'MISC'), (24, 27, 'MISC')]}),
    ('qual item você gostaria a b ou c', {'entities': [(2, 3, 'MISC'), (26, 27, 'MISC'), (12, 13, 'MISC')]}),
    ('qual é a resposta correta a b ou c', {'entities': [(2, 3, 'MISC'), (28, 29, 'MISC'), (18, 19, 'MISC')]}),
    ('qual item você gostaria um chá um café ou um refrigerante', {'entities': [(27, 30, 'MISC'), (34, 38, 'MISC'), (45, 57, 'MISC')]}),
]

ner = ner_controller()
model = ner.create_model()

results = evaluate(model, examples)
print(results)