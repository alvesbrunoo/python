gameList = ['Resident Evil 4', 'Star Wars Jedi Survivor',
            'The Legend of Zelda', 'Red Dead 2', 'Mario Odyssey']

# 1 - Tamanho da lista pelo índice
print(len(gameList))

# 2 - recuperar um item da lista pelo índice 
print(gameList.index('Mario Odyssey'))

# 3 - Adicionmare o item ao final da lista
gameList.append('GTA V')
print(gameList)

# 4 - Ordernar a lista
gameList.sort()
print(gameList)

# 5 - Copia os itens de uma lista para o outra
gameReset = gameList.copy()
gameReset.remove('Star Wars Jedi Survivor')
print(gameReset)

# 6 - remove todos os dados da lista
gameList.clear()
print(gameList)