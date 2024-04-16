name = input('Digite o nome do jogo:\n ')
year = int(input('Digite o ano de lançamento do jogo:\n '))
gamePrice = float(input('Digite o preço do jogo:\n '))
planIncluded = input('Está incluso no serviço mensal? ')

print(f'O nome do jogo é {name}')
print(f'O ano de lançamento é {year}')
print(f'O preço do jogo é {gamePrice}')

if planIncluded == 'True':
    print('Está incluso no serviço mensal')
if planIncluded == 'False': 
    print('Não está incluso no serviço mensal')