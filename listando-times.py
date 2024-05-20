team = {}
done = False

def printTeam():
    print('Times listados:')
    for i, team in enumerate(team.values()):
        print(f'{i+1}. {team['name']} (len{team['players']} jogadores)')
        
while not done:
    print('O que você deseja fazer?')
    print('1. Adicionar um time')
    print('2. Remover um time')
    print('3. Listar time')
    print('4. Adicionar jogador em um time')
    print('5. Remover jogador em um time')
    print('6. Listar jogadores em um time')
    print('7. Sair')
    
    choice = input('>')
    
    if choice == '1':
        teamName = input('Digite o nome do time:\n')
        team[teamName] = {'name': teamName, 'players': []}
        print('Time adicionado')
    
    elif choice == '2':
        teamNum = int(input('Informe o número do time que deseja remover\n'))
        if teamNum <= len(team):
            teamName = list(team.keys())[teamNum - 1]
            del team[teamName]
            print('Time removido')
    
    elif choice == '3':
        printTeam()