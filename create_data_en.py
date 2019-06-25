import pandas as pd

def sentence_to_train_format(sentence, entities):
    formated_sentence = []
    formated_sentence.append("('" + sentence + "', {'entities': [")          
    for i in range(len(entities)):
        entity = entities[i].strip()
        start_index = str(get_word_position(sentence, entity))
        end_index = str(get_word_position(sentence, entity) + len(entity))
        entity = "(" + start_index + ", " + end_index  +", "+ "'MISC')"
        if i < len(entities) - 1:
            formated_sentence.append(entity + ", ")
        else:
            formated_sentence.append(entity + "]}),")
    return ''.join(formated_sentence)

def go_to_sentence(i, j):
    sentence = 'do you want to go to the {0} or to the {1}'.format(i,j)
    entities = [i,j]
    return sentence_to_train_format(sentence, entities)

def want_x_or_y_sentence(i,j):
    sentence = 'do you want {0} or {1}'.format(i,j)
    entities = [i,j]
    return sentence_to_train_format(sentence, entities)

def want_x_y_or_z_sentence(verb, i,j,k):
    sentence = 'you want {3} {0} {1} or {2}'.format(i,j,k, verb)
    entities = [i,j,k]
    return sentence_to_train_format(sentence, entities)

def want_with_or_without(i, j):
    sentence = 'do you want {0} with or without {1}'.format(i,j)
    entities = ["with", "without"]
    return sentence_to_train_format(sentence, entities)

def affirmative_questions(i, j, k):
    sentence = 'the result is {0} {1} or {2}'.format(i,j,k)
    entities = [i, j, k]
    return sentence_to_train_format(sentence, entities)

def get_word_position(sentence, word):
    print(sentence)
    print(word)
    return sentence.index(word)




def read_csv(path_arq):
    columns_df = []
    rows_df = []
    ler_dados = False
    
    with open(path_arq) as fp:
        linha = fp.readline()
        while linha:
            linha = fp.readline()
            if("@attribute" in linha):
                tag ,feature, valores = linha.split(" ")
                columns_df.append(feature)
            if("@data" in linha):
                ler_dados = True
            if(ler_dados):
                valores = linha.split(",")
                rows_df.append(valores)
                
    df = pd.DataFrame(rows_df, columns = columns_df)
    df.dropna(inplace = True)
    df = df.astype('int')
    return df   

verbs = ['want', 'like', 'wish', 'apreciate', 'pretend', 'plan', 'need', 'choose', 'love', 'eat', 'approve']

def create_list(index):
    if index == 0:
        lista_comidas = ['banana', 'apple', 'salad', 'fruit', 'vanilla', 'pizza', 'hamburguer','chocolate',
        'rice','a','b','c']
        return lista_comidas
    elif index == 1:
        lista_lugares = ['a','b','c','grandmother', 'school', 'therapy', 'park','shopping','club','chess']
        return lista_lugares
    elif index == 2:
        lista_acoes = ['a','b','c','play', 'run', 'lift','jump', 'sleep', 'dream', 'fly', 'work', 'live']
        return lista_acoes


def generate_training_data(train_file):
    f = open(train_file, 'a')
    for list_type in range(3):
        lista = create_list(list_type)
        if list_type == 0:
            for i in lista:
                if lista.index(i) < len(lista) - 1:
                    sentence = want_with_or_without(i, lista[lista.index(i)+1])
                    f.write(sentence + '\n')
                if lista.index(i) < len(lista) - 2:
                    verb = verbs[lista.index(i)]
                    sentence = want_x_y_or_z_sentence(verb, i, lista[lista.index(i)+1], lista[lista.index(i)+2])
                    f.write(sentence + '\n')
        elif list_type == 1:
            for i in lista:
                if lista.index(i) != len(lista) - 1:
                    sentence = go_to_sentence(i, lista[lista.index(i)+1])
                    f.write(sentence + '\n')
        elif list_type == 2:
            for i in lista:
                if lista.index(i) != len(lista) - 1:
                    sentence = want_x_or_y_sentence(i, lista[lista.index(i)+1])
                    f.write(sentence + '\n')
                if lista.index(i) < len(lista) - 2:
                    sentence = affirmative_questions(i, lista[lista.index(i)+1], lista[lista.index(i)+2])
                    f.write(sentence + '\n')
            
        
    f.close()



def create_train_with_csv(data_path, train_file):
    df = pd.read_csv(data_path)

    f = open(train_file, 'w+')
    f.write('TRAIN_DATA = [')

    for i in range(len(df)):
        sentence = df.ix[i,0].lower()
        entities = df.ix[i,1].split(',')
        train_sample = sentence_to_train_format(sentence, entities)
        f.write(train_sample + '\n')
    f.close()
'''          
def create_phrases_through_template(file_path):
    df = pd.read_csv(data_path)

    f = open(train_file, 'a')

    for i in range(len(df)):
        sentence = df.ix[i,0].lower()
        entities = df.ix[i,1].split(',')
        
        for entity in entities:
            
            sentence.replace(entity, )


        f.write(train_sample + '\n')
    f.close()
'''
    

create_train_with_csv('Frases - ENG.csv', 'train_data_en.py')
generate_training_data('train_data_en.py')
f = open('train_data_en.py', 'a')
f.write(']')
f.close()