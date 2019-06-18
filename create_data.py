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
    sentence = 'voce quer ir a {0} ou ao {1}'.format(i,j)
    entities = [i,j]
    return sentence_to_train_format(sentence, entities)

def want_x_or_y_sentence(i,j):
    sentence = 'voce gostar {0} ou {1}'.format(i,j)
    entities = [i,j]
    return sentence_to_train_format(sentence, entities)

def want_x_y_or_z_sentence(verb, i,j,k):
    sentence = 'voce {3} {0} {1} ou {2}'.format(i,j,k, verb)
    entities = [i,j,k]
    return sentence_to_train_format(sentence, entities)

def want_with_or_without(i, j):
    sentence = 'voce quer {0} com ou sem {1}'.format(i,j)
    entities = ["com", "sem"]
    return sentence_to_train_format(sentence, entities)

def affirmative_questions(i, j, k):
    sentence = 'o resultado é {0} {1} ou {2}'.format(i,j,k)
    entities = [i, j, k]
    return sentence_to_train_format(sentence, entities)

def get_word_position(sentence, word):
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

verbs = ['quer', 'gostar', 'desejar', 'apreciar', 'pretender', 'planejar', 'precisar', 'escolher', 'optar', 'preferir', 'adorar', 'amar', 'comer', 'aprovar', 'experimentar' ,'fazer', 'realizar', 'praticar', 'conhecer', 'ir', 'contar', 'criar']

def create_list(index):
    if index == 0:
        lista_comidas = ['banana', 'maça', 'salada', 'fruta', 'baunilha', 'pizza', 'hamburguer', 'prestigio','chocolate',
        'rapadura','arroz','a','b','c']
        return lista_comidas
    elif index == 1:
        lista_lugares = ['a','b','c','casa da vo', 'escola', 'cyber', 'terapia', 'parque','shopping','nataçao','clube','xadrez']
        return lista_lugares
    elif index == 2:
        lista_acoes = ['a','b','c','brincar', 'correr', 'levantar','pular', 'jogar','deitar','dormir', 'sonhar', 'voar', 'trabalhar', 'fugir','viver']
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
            


create_train_with_csv('Frases - PT.csv', 'train_data.py')
generate_training_data('train_data.py')
f = open('train_data.py', 'a')
f.write(']')
f.close()