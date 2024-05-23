import re

text = 'OneBitCode: Transformamos pessoas em programadores sem limites'

# O 'r' significa que estamos trabalhanodo com string bruta (row string)

# 1 - Índice iniciall e final de palavras
match = re.search(r'pessoas em programadores', text)
print('Índice inicial', match.start())
print('Índice finall', match.end())

# 2 - Buscando o índice que possui o ponto
site = 'https://onebitcode.com'
match = re.search(r'\.', site)
print(match)

# 3 - Buscando uma lista de caracteres dentro de uma lista
pattern = '[a-m]'
result = re.findall(pattern, text)
print(text)
print(result)

# 4 - Verificando o ínicio de uma string
rule = r'^A'
phrases = ['A casa está suja', 'O dia está lindo', 'Vamos passear']
for p in phrases:
    if re.match(rule, p):
        print(f'Corresponde: {p}')
    else:
        print(f'Não corresponde: {p}')

# 5 - Verificando o final de uma string
ruleEnd = r'!$'
phrases = 'O dia está lindo!'
match = re.search(ruleEnd, phrases)
if match:
    print('Sim, corresponde')
else:
    print('Não, corresponde')
