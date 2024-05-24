import random

done = False

while not done:
    print('O que você deseja fazer?')
    print('1. Adivinhar o número')
    print('2. Sair')
    
    choice = input('>')
    
    if choice == '1':
        numero = int(input('Escolha um númerod e 1 a 10:\n'))
        r1 = random.randint(1, 10)
        if numero == r1:
            print('Acertou!')
        else:
            print(f'Errou! o número sorteado foi {r1}')
    elif choice == '2':
        done = True
    else:
        print('Opção inválida')
    