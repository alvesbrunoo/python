number = int(input('Tabuada do:\n'))
begin = int(input('Do:\n'))
end = int(input('Até:\n'))

x = begin

while x <= end:
    print(f'Tabuada do {number} x {x} = {number * x}')
    x += 1