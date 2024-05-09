name = input('Digite o nome do jogo\n')
yearlaunch = int(input('Digite o ano de lançamento do jogo\n'))
classification = float(input('Digite a note de classificação do jogo\n'))

if classification > 8.0 and yearlaunch >= 2015:
    print(f'O jogo {name} é bom. Recomendo jogá-lo')
else:
    print(f'O jogo {name} ainda não atingiu uma nota boa. Por isso não recomendo')