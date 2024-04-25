gamesSet = {"Fifa23", "Red Dead 2", "Star Wars", "The Legend of Zelda", "Red Dead 2"}
print(gamesSet)

# 1 - Buscar o tamanho do set
print(len(gamesSet))

# 2 - True e 1 são considerados o mesmo valor
exempleSet = {'Fifa23', True, 1, 90.50}
print(exempleSet)

# 3 - Adicionar item de outro set
gamesSet.update(exempleSet)
print(gamesSet)

# 4 - remover um item no set
gamesSet.remove(True)
gamesSet.remove(90.5)
print(gamesSet)

# Não possibilita recuperar valores via fatiamente ou slice