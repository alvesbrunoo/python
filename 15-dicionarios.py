gameFifa = {
    "price": 90.55,
    "yearLaunch": 2022,
    "version": 2023,
    "classification": 8.5,
    "genre": ["esporte", "família"]
}

print(gameFifa)
# print(len(gameFifa))
# print(type(gameFifa))

# 1 - Recuperar um elemento do dicionário
print(gameFifa['genre']) # As duas maneiras dão certo
print(gameFifa.get('classification'))

# 2 - Buscar apenas as chaves do dicionário	
print(gameFifa.keys())

# 3 - Buscar apenas os valores so dicionário
print(gameFifa.values())

# 4 - Adicionar itens no dicionário
gameFifa['players'] = 2
print(gameFifa)

# 5 - Atualizar itens no dicionário
gameFifa.update({'players': 1})
print(gameFifa)

# 6 - Buscar itens no dicionário
print(gameFifa.items())

# 7 - Remover item no dicionário
gameFifa.pop('players')
print(gameFifa)