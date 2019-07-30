import re

a = re.compile(r'(\w+ (de|da) \w+)|(\w+ \w+)')

text = 'pizza de frango calabresa da queijo'
text = 'cachorro quente'
busca = a.findall(text)
print(busca)