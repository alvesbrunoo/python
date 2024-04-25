gameName = 'Fifa23'
gameDescription = '''
Fifa 23 é um jogo de futebol
desenvolvido pela EA Sports,
e que possibilita jogar 
localmente ou online.
'''

print(gameName.upper()) # Retorna string em maiúsculo
print(gameName.lower()) # Retorna string em minúsculo
print(gameName.capitalize()) # Apenas a primeira letra em maiúsculo
print(gameName.title()) # Apenas a primeira letra em maiúsculo
print(gameName.center(10, '-')) # Retorna string centralizada com caractere de preenchimento
print(gameName.find('i')) # Retorna a posição de um determinado caracterer
print(gameDescription.count('f')) # Conta caracter
print(gameDescription.count('a')) # Conta caracter
print(gameDescription.replace('Fifa', 'Pes')) # Altera um elemento por outro
print(gameDescription.split(',')) # Quebra a string
