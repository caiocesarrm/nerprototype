from flair.data import Sentence
from flair.models import SequenceTagger

'''

# make a sentence
sentence = Sentence('I love Berlin .')

# load the NER tagger
tagger = SequenceTagger.load('ner-multi')
b = 2
print('ready')
def teste(frase, tagger_criado):
    sentence = Sentence(frase)

    # predict NER tags
    tagger_criado.predict(sentence)

    # print sentence with predicted tags
    print(sentence.to_tagged_string())
    # iterate over entities and print
    for entity in sentence.get_spans('ner'):
        print(entity)

while True:
    a = input()
    teste(a, tagger)
'''
from typing import List
from flair.training_utils import EvaluationMetric
from flair.embeddings import StackedEmbeddings, WordEmbeddings, FlairEmbeddings, BytePairEmbeddings, TokenEmbeddings
from flair.trainers import ModelTrainer
import flair.datasets
from pathlib import Path
'''
#corpus = flair.datasets.WIKINER_PORTUGUESE()
corpus = flair.datasets.WIKINER_PORTUGUESE().downsample(0.2)
tag_type = 'ner'

print(len(corpus.train))
print(len(corpus.test))
print(len(corpus.dev))



print("--- 1 Original ---")
print(corpus)


print('dict')
tag_dictionary = corpus.make_tag_dictionary(tag_type)
print(corpus.make_tag_dictionary(tag_type))

print('stats')
stats = corpus.obtain_statistics()
print(stats)

embedding_types: List[TokenEmbeddings] = [

    WordEmbeddings('glove'),

    # comment in this line to use character embeddings
    # CharacterEmbeddings(),

    # comment in these lines to use flair embeddings
    # FlairEmbeddings('news-forward'),
    # FlairEmbeddings('news-backward'),
]

embeddings: StackedEmbeddings = StackedEmbeddings(embeddings=embedding_types)

from flair.models import SequenceTagger

tagger: SequenceTagger = SequenceTagger(hidden_size=256,
                                        embeddings=embeddings,
                                        tag_dictionary=tag_dictionary,
                                        tag_type=tag_type,
                                        use_crf=True)

# 6. initialize trainer
from flair.trainers import ModelTrainer

trainer: ModelTrainer = ModelTrainer(tagger, corpus)

# 7. start training
trainer.train('resources/taggers/example-ner',
              learning_rate=0.1,
              mini_batch_size=32,
              max_epochs=1)


# load the model you trained

model = SequenceTagger.load('resources/taggers/example-ner/final-model.pt')

print('Ready')
def teste(frase, modelo):
    sentence = Sentence(frase)
    modelo.predict(sentence)
    print(sentence.to_tagged_string())

while True:
    user_input = input()
    teste(user_input, model)





'''

tagger = SequenceTagger.load('pos-multi')

# text with English and German sentences
sentence = Sentence('George Washington went to Washington . Dort kaufte er einen Hut .')

# predict PoS tags
tagger.predict(sentence)

# print sentence with predicted tags
print(sentence.to_tagged_string())

print('Ready')
def teste(frase, modelo):
    sentence = Sentence(frase)
    modelo.predict(sentence)
    print(sentence.to_tagged_string())

while True:
    user_input = input()
    teste(user_input, tagger)