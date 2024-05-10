gameList = ['Fifa 23', 'God of War', 'Red dead 2', 'Uncharted', 90.5]

# 1 - Iterando valores de uma lista
# for game in gameList:
#     print(game)

# 2 - Quando a condição for atendida, o loop será encerrado 
# for game in gameList:
#     if game == 'Red dead 2':
#         break
#     print(game)
    
# 3 - Quando a condição for atendida, o loop vai para a próxima iração
# for game in gameList:
#     if game == 'Red dead 2':
#         continue
#     print(game) 
    
# 4 - Avaliação do jogo

gameName = input('Digite o nome do jogo:\n')
gameRating = int(input('Digite quantas avaliações deseja fazer no jogo:\n'))

sum = 0 
for i in range(gameRating):
    note = float(input('Digite a nota para o jogo:'))
    sum += note
print(f'Média da avaliação do jogo {gameName} é {sum/gameRating :.2f}')
