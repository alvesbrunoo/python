# 1 - Fatorial de um número

def fatorial(num):
    if num == 1:
        return 1
    else:
        return(num * fatorial(num - 1))
number = int(input('Digite o número para o fatorial:\n'))
print(f'O fatorial do número {number} é: {fatorial(number)}')

        

# 2 - Soma total de um número 

def soma(num):
    if num == 1:
        return 1
    else:
        return(num + soma(num - 1))
number = int(input('Digite o número para o fatorial:\n'))
print(f'O fatorial do número {number} é: {soma(number)}')