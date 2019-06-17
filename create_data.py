import pandas as pd
def go_to_sentence(i, j):
    sentence = 'voce quer ir {0} ou ao {1}'.format(i,j)
    start_1 = str(get_word_position(sentence, i))
    end_1 = str(get_word_position(sentence, i) + len(i))
    start_2 = str(get_word_position(sentence, j))
    end_2 = str(get_word_position(sentence, j) + len(j))
    entity_1 = "(" + start_1 + ", " + end_1  +", "+ "'MISC')"
    entity_2 = "(" + start_2 + ", " + end_2  +", "+ "'MISC')"
    formated_sentence = "('" + sentence + "', {'entities': [" + entity_1 + ", " + entity_2 + "]}),"
    return formated_sentence

def want_x_or_y_sentence(i,j):
    return 'voce quer {0} ou {1}'.format(i,j)

def want_x_y_or_z_sentence(i,j,k):
    return 'voce quer {0} {1} ou {2}'.format(i,j,k)

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


def create_list(index):
    if index == 0:
        lista_comidas = ['banana', 'maça', 'salada', 'fruta', 'baunilha', 'pizza', 'hamburguer', 'prestigio','chocolate',
        'rapadura','arroz']
        return lista_comidas
    elif index == 1:
        lista_lugares = ['casa da vo', 'escola', 'cyber', 'terapia', 'parque','shopping']
        return lista_lugares
    elif index == 2:
        lista_acoes = ['brincar', 'correr', 'levantar','pular', 'jogar','deitar','dormir']
        return lista_acoes


def generate_training_data(train_file):
    f = open(train_file, 'a')
    for list_type in range(3):
        lista = create_list(list_type)
        for i in lista:
            if lista.index(i) != len(lista) - 1:
                sentence = go_to_sentence(i, lista[lista.index(i)+1])
                f.write(sentence + '\n')
    f.close()



def create_train_with_csv(data_path, train_file):
    df = pd.read_csv(data_path)

    f = open(train_file, 'w+')
    f.write('TRAIN_DATA = [')

    for i in range(len(df)):
        sentence = df.ix[i,0].lower()
        entities = df.ix[i,1].split(',')
        choices = []
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

        train_sample = ''.join(formated_sentence)
        f.write(train_sample + '\n')
    f.close()
            

            
create_train_with_csv('Frases - PT.csv', 'train_data.py')
generate_training_data('train_data.py')
f = open('train_data.py', 'a')
f.write(']')
f.close()