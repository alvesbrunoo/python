def checkChar(text):
    type = {'Uppercase': 0, 'Lowercase': 0}
    for char in text:
        if char.isupper():
            type['Uppercase'] +=1
        elif char.islower():
            type['Lowercase'] +=1
    print('Texto original:', text)
    print('Número de letras maiúsculas:', type['Uppercase'])
    print('Número de letras minúsculas:', type['Lowercase'])
checkChar('A Melhor Forma De Prever oFuturo é Criá-lo')

def checkNumbers(numbers):
    pairs = []
    odd = []
    for number in numbers:
        if number % 2  == 0:
            pairs.append(number)
        else:
            odd.append(number)
    return pairs, odd
print(checkNumbers([1, 2, 4, 6, 5, 7, 11, 20]))