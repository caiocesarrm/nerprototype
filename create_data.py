
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

f = open('train_data.py', 'w+')

f.write('TRAIN_DATA = [')

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

for list_type in range(3):
    lista = create_list(list_type)
    for i in lista:
        if lista.index(i) != len(lista) - 1:
            sentence = go_to_sentence(i, lista[lista.index(i)+1])
            f.write(sentence + '\n')

f.write(']')
f.close()

    

