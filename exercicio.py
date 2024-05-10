# Cáculo da distância

# distance = float(input('Digite a distância a percorrer\n'))

# if distance <= 200:
#     ticket = 0.5 * distance
# else:
#     ticket = 0.35 * distance
# print(f'O preço da passagem é {ticket:.2f}')

# Aumento de salário de funcionário

salary = float(input('Digite o seu salário\n'))
perc_incrense = 0.15

if perc_incrense > 1250:
    perc_incrense = 0.10
incrense = salary * perc_incrense
print(f'Seu aumento será de {incrense:.2f}')