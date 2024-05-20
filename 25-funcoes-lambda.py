# 1 - funções de potência de número
power = lambda x : x ** 2 

# 2 - Função que verifica se o número é par ou par
pair = lambda x : x % 2 == 0

# 3 - Função que divide um número por outro
divNum = lambda x, y : x / y

# 4 - Função que inverte uma string
reverse = lambda x : x[::-1]

print(power(5))
print(pair(10))
print(pair(5))
print(divNum(20, 2))
print(reverse('JavaScript'))