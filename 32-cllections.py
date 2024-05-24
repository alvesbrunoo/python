from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Contar itens de uma lista
fruits = ['Maça' , 'Banana', 'Uva', 'Pêra', 'Banana',
          'Uva', 'Maçã', 'Laranja', 'Banana', 'Abacaxi',
          'Tangerina', 'Uva', 'Pêra', 'Banana']
print(fruits)
print(Counter(fruits))

print('-' * 20)

# 2 - Utlizando tupla nomeada
game = namedtuple('game', ['name', 'price', 'note'])
g1 = game('Fifa23', 90.50, 8.5)
g2 = game('Resident Evil 4 Remake', 300, 10.00)
print(g1)
print(g2)

print('-' * 20)

# 3 - Ordenando dicionários
studants = {'Pedro':23, 'Ana':22, 'Ronaldo':26, 'Janaína':25}
a = sorted(studants.items(), key=itemgetter(0))
print(studants)
print(a)

print('-' * 20)

# 4 - utilizando fila ambas extremidades
deq = deque([20, 40, 60, 80])
deq.appendleft(10)
print(deq)
deq.append(50)
print(deq)
deq.popleft()
print(deq)
deq.pop()
print(deq)