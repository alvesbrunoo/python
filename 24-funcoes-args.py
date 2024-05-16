"""
*args - Utilizamos ele quando não temos certeza de quantos argumentos queremos ter numa função
- Os argumentos são passados como uma tupla

**kwargs - Além dos valores podemos passar também as respectivas chaves para cada argumento.
- Os valores são passados como um dicionário
"""

# 1 - Soma de números

def sum(*num):
    sumTotal = 0
    for n in num:
        sumTotal += n
    print(f'Soma é: {sumTotal}')

sum(7)
sum(7, 9)
sum(7, 9, 10, 11)
sum(7, 9, 10, 8, 6, 7)

# 2 - Apresentação de cursos

def presentation(**data):
    for key, value in data.items():
        print(f'{key} - {value}')

presentation(name='Python', category='Back-end', level='Iniciante')
presentation(name='Visão Computacional', category='IA', level='Avançado')
presentation(name='Dashboard com Dash', category='Back-end', level='Iniciante')
