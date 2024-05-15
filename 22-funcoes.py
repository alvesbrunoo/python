# 1 - Funçãopara imprimir 'Hello World'

def wellcome():
    print('Hello World')
wellcome()

# 2 - Função para somar dois números

def sum():
    return 5 +4
print(sum())

# 3 - Função para cadastrar um jogo

def createGame():
    name = input('Digite o nome do jogo:\n')
    yearLaunch = int(input('Digite o ano e lançamento do jogo:\n'))
    gamePrice = float(input('Digite o preço do jogo:\n'))
    noteRating = float(input('Digite a nota de avaliação do jogo:\n'))
    print(f'{name} - R$ {gamePrice}')
createGame()
createGame()