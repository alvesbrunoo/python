import re

def checkCharacter(string):
    rule = re.compile(r'[^a-zA-Z0-9]')
    string = rule.search(string)
    return not bool(string)

print(checkCharacter('GHDGAssjhvg908867'))
print(checkCharacter('{}6765cyhgHGHTG#$'))