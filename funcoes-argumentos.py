# 1 - crie uma fução que receba dois argumentos: o primeiro nome e o segundo nome

def fullName(fname, lname):
    print(f'Nome completo: {fname} {lname}')
fullName('Bruno', 'Alves')

# 2 - Crie uma função que some dois números via parâmetros 

def sum(a, b):
    return a + b
print(sum(10, 50))

# 3 - Argumentos default numa função 

def address(country='Brasil'):
    print(f'Eu moro no {country}')
address()
address('Estados Unidos')

# 4 - Avaliação do jogo

def ratingGame(qdtRating):
    gameName = input('Digite o nome do jogo:\n')
    sum = 0
    for i in range(qdtRating):
        note = float(input('Digite a nota para o jogo:\n'))
        sum += note
    print(f'A média do jogo {gameName} é: {sum/ qdtRating}')

rating = int(input('Digite quantas avaliações deseja fazer no jogo:\n'))
ratingGame(rating)
ratingGame(rating)