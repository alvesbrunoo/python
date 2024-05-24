import random

# 1 - Seleciona valor aleatório de uma lista
list = [7, 6, 4, 3, 2, 1]
print(list)

# 2 - Gera um número em um intervalo de valores
r1 = random.randint(5, 15)
print(r1)

# 3 - Seleciona caractere aleatório de uma string
name = 'Curso Python'
r2 = random.choice(name)
print(r2)

# 4 - Selecione mais de um valor aleatório
print(random.sample(list, 2))
print(random.sample(list, 3))
s = 'Olá Mundo!'
print(random.sample(s, 2))