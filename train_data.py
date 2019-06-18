TRAIN_DATA = [('voce quer comer batata frita cachorro quente ou hamburguer', {'entities': [(16, 28, 'MISC'), (29, 44, 'MISC'), (48, 58, 'MISC')]}),
('voce está triste ou cansado', {'entities': [(10, 16, 'MISC'), (20, 27, 'MISC')]}),
('você está com fome ou com sede', {'entities': [(14, 18, 'MISC'), (26, 30, 'MISC')]}),
('voce quer uma duas ou tres colheres', {'entities': [(10, 13, 'MISC'), (14, 18, 'MISC'), (22, 26, 'MISC')]}),
('você quer água suco refrigerante ou limonada', {'entities': [(10, 14, 'MISC'), (15, 19, 'MISC'), (20, 32, 'MISC'), (36, 44, 'MISC')]}),
('é uma resposta fotópica ou escotópica', {'entities': [(15, 23, 'MISC'), (27, 37, 'MISC')]}),
('o índice é 1 ou 1.33', {'entities': [(11, 12, 'MISC'), (16, 20, 'MISC')]}),
('quantos anos você tem 7 ou 8', {'entities': [(22, 23, 'MISC'), (27, 28, 'MISC')]}),
('você gosta de frutas doces ou azedas', {'entities': [(21, 26, 'MISC'), (30, 36, 'MISC')]}),
('você quer uma fruta azeda ou doce', {'entities': [(20, 25, 'MISC'), (29, 33, 'MISC')]}),
('você prefere android ou ios', {'entities': [(13, 20, 'MISC'), (24, 27, 'MISC')]}),
('qual item você gostaria a b ou c', {'entities': [(2, 3, 'MISC'), (26, 27, 'MISC'), (12, 13, 'MISC')]}),
('qual é a resposta correta a b ou c', {'entities': [(2, 3, 'MISC'), (28, 29, 'MISC'), (18, 19, 'MISC')]}),
('qual item você gostaria um chá um café ou um refrigerante', {'entities': [(27, 30, 'MISC'), (34, 38, 'MISC'), (45, 57, 'MISC')]}),
('voce quer fritas hambúrguer feijao ou arroz', {'entities': [(10, 16, 'MISC'), (17, 27, 'MISC'), (28, 34, 'MISC'), (38, 43, 'MISC')]}),
('voce quer dormir andar comer ou sonhar', {'entities': [(10, 16, 'MISC'), (17, 22, 'MISC'), (23, 28, 'MISC'), (32, 38, 'MISC')]}),
('voce quer dormir com ou sem travesseiro', {'entities': [(17, 20, 'MISC'), (24, 27, 'MISC')]}),
('voce quer banana com ou sem maça', {'entities': [(17, 20, 'MISC'), (24, 27, 'MISC')]}),
('voce quer banana maça ou salada', {'entities': [(10, 16, 'MISC'), (17, 21, 'MISC'), (25, 31, 'MISC')]}),
('voce quer maça com ou sem salada', {'entities': [(15, 18, 'MISC'), (22, 25, 'MISC')]}),
('voce gostar maça salada ou fruta', {'entities': [(12, 16, 'MISC'), (17, 23, 'MISC'), (27, 32, 'MISC')]}),
('voce quer salada com ou sem fruta', {'entities': [(17, 20, 'MISC'), (24, 27, 'MISC')]}),
('voce desejar salada fruta ou baunilha', {'entities': [(13, 19, 'MISC'), (20, 25, 'MISC'), (29, 37, 'MISC')]}),
('voce quer fruta com ou sem baunilha', {'entities': [(16, 19, 'MISC'), (23, 26, 'MISC')]}),
('voce apreciar fruta baunilha ou pizza', {'entities': [(14, 19, 'MISC'), (20, 28, 'MISC'), (32, 37, 'MISC')]}),
('voce quer baunilha com ou sem pizza', {'entities': [(19, 22, 'MISC'), (26, 29, 'MISC')]}),
('voce pretender baunilha pizza ou hamburguer', {'entities': [(15, 23, 'MISC'), (24, 29, 'MISC'), (33, 43, 'MISC')]}),
('voce quer pizza com ou sem hamburguer', {'entities': [(16, 19, 'MISC'), (23, 26, 'MISC')]}),
('voce planejar pizza hamburguer ou prestigio', {'entities': [(14, 19, 'MISC'), (20, 30, 'MISC'), (34, 43, 'MISC')]}),
('voce quer hamburguer com ou sem prestigio', {'entities': [(21, 24, 'MISC'), (28, 31, 'MISC')]}),
('voce precisar hamburguer prestigio ou chocolate', {'entities': [(14, 24, 'MISC'), (25, 34, 'MISC'), (38, 47, 'MISC')]}),
('voce quer prestigio com ou sem chocolate', {'entities': [(20, 23, 'MISC'), (27, 30, 'MISC')]}),
('voce escolher prestigio chocolate ou rapadura', {'entities': [(14, 23, 'MISC'), (24, 33, 'MISC'), (37, 45, 'MISC')]}),
('voce quer chocolate com ou sem rapadura', {'entities': [(20, 23, 'MISC'), (27, 30, 'MISC')]}),
('voce optar chocolate rapadura ou arroz', {'entities': [(11, 20, 'MISC'), (21, 29, 'MISC'), (33, 38, 'MISC')]}),
('voce quer rapadura com ou sem arroz', {'entities': [(19, 22, 'MISC'), (26, 29, 'MISC')]}),
('voce preferir rapadura arroz ou a', {'entities': [(14, 22, 'MISC'), (23, 28, 'MISC'), (15, 16, 'MISC')]}),
('voce quer arroz com ou sem a', {'entities': [(16, 19, 'MISC'), (23, 26, 'MISC')]}),
('voce adorar arroz a ou b', {'entities': [(12, 17, 'MISC'), (5, 6, 'MISC'), (23, 24, 'MISC')]}),
('voce quer a com ou sem b', {'entities': [(12, 15, 'MISC'), (19, 22, 'MISC')]}),
('voce amar a b ou c', {'entities': [(5, 6, 'MISC'), (12, 13, 'MISC'), (2, 3, 'MISC')]}),
('voce quer b com ou sem c', {'entities': [(12, 15, 'MISC'), (19, 22, 'MISC')]}),
('voce quer ir a casa da vo ou ao escola', {'entities': [(15, 25, 'MISC'), (32, 38, 'MISC')]}),
('voce quer ir a escola ou ao cyber', {'entities': [(15, 21, 'MISC'), (28, 33, 'MISC')]}),
('voce quer ir a cyber ou ao terapia', {'entities': [(15, 20, 'MISC'), (27, 34, 'MISC')]}),
('voce quer ir a terapia ou ao parque', {'entities': [(15, 22, 'MISC'), (29, 35, 'MISC')]}),
('voce quer ir a parque ou ao shopping', {'entities': [(15, 21, 'MISC'), (28, 36, 'MISC')]}),
('voce quer ir a shopping ou ao nataçao', {'entities': [(15, 23, 'MISC'), (30, 37, 'MISC')]}),
('voce quer ir a nataçao ou ao clube', {'entities': [(15, 22, 'MISC'), (29, 34, 'MISC')]}),
('voce quer ir a clube ou ao xadrez', {'entities': [(15, 20, 'MISC'), (27, 33, 'MISC')]}),
('voce gostar brincar ou correr', {'entities': [(12, 19, 'MISC'), (23, 29, 'MISC')]}),
('o resultado é brincar correr ou levantar', {'entities': [(14, 21, 'MISC'), (22, 28, 'MISC'), (32, 40, 'MISC')]}),
('voce gostar correr ou levantar', {'entities': [(12, 18, 'MISC'), (22, 30, 'MISC')]}),
('o resultado é correr levantar ou pular', {'entities': [(14, 20, 'MISC'), (21, 29, 'MISC'), (33, 38, 'MISC')]}),
('voce gostar levantar ou pular', {'entities': [(12, 20, 'MISC'), (24, 29, 'MISC')]}),
('o resultado é levantar pular ou jogar', {'entities': [(14, 22, 'MISC'), (23, 28, 'MISC'), (32, 37, 'MISC')]}),
('voce gostar pular ou jogar', {'entities': [(12, 17, 'MISC'), (21, 26, 'MISC')]}),
('o resultado é pular jogar ou deitar', {'entities': [(14, 19, 'MISC'), (20, 25, 'MISC'), (29, 35, 'MISC')]}),
('voce gostar jogar ou deitar', {'entities': [(12, 17, 'MISC'), (21, 27, 'MISC')]}),
('o resultado é jogar deitar ou dormir', {'entities': [(14, 19, 'MISC'), (20, 26, 'MISC'), (30, 36, 'MISC')]}),
('voce gostar deitar ou dormir', {'entities': [(12, 18, 'MISC'), (22, 28, 'MISC')]}),
('o resultado é deitar dormir ou sonhar', {'entities': [(14, 20, 'MISC'), (21, 27, 'MISC'), (31, 37, 'MISC')]}),
('voce gostar dormir ou sonhar', {'entities': [(12, 18, 'MISC'), (22, 28, 'MISC')]}),
('o resultado é dormir sonhar ou voar', {'entities': [(14, 20, 'MISC'), (21, 27, 'MISC'), (31, 35, 'MISC')]}),
('voce gostar sonhar ou voar', {'entities': [(12, 18, 'MISC'), (22, 26, 'MISC')]}),
('o resultado é sonhar voar ou trabalhar', {'entities': [(14, 20, 'MISC'), (21, 25, 'MISC'), (29, 38, 'MISC')]}),
('voce gostar voar ou trabalhar', {'entities': [(12, 16, 'MISC'), (20, 29, 'MISC')]}),
('o resultado é voar trabalhar ou fugir', {'entities': [(14, 18, 'MISC'), (19, 28, 'MISC'), (32, 37, 'MISC')]}),
('voce gostar trabalhar ou fugir', {'entities': [(12, 21, 'MISC'), (25, 30, 'MISC')]}),
('o resultado é trabalhar fugir ou viver', {'entities': [(14, 23, 'MISC'), (24, 29, 'MISC'), (33, 38, 'MISC')]}),
('voce gostar fugir ou viver', {'entities': [(12, 17, 'MISC'), (21, 26, 'MISC')]}),
]