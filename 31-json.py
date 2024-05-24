import json

# 1 - Strings para dicionários
person = '{"name":"Bruno", "languagens":["Python", "JavaScript"]}'
personDict = json.loads(person)
# print(personDict)
# print(personDict['languagens'])

# 2 - Convertendo dicionários para json
personJson = json.dumps(personDict)
print(personJson)
print(type(personJson))
print(type(personDict))

# 3 - Formatando Json
print(json.dumps(personDict, indent =4, sort_keys=True))

# 4 - Salvando json em txt
with open('person.txt', 'w') as jsonFile:
    json.dump(personDict, jsonFile)
    
