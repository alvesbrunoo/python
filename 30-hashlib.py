import hashlib

# 1 - Verificar os algoritimos disponíveis
print(hashlib.algorithms_available)

print('-' * 20)

# 2 - Algoritmos disponíveis de acordo com SO
print(hashlib.algorithms_guaranteed)

#  3- Utilizando o Sha256
algorithm = hashlib.sha256()
print(algorithm.digest())
message = 'A melhor forma de prever o futuro é criá-lo'.encode()
algorithm.update(message)
print(algorithm.hexdigest())

print('-' * 20)

# 4 - Utilizando o MD5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())