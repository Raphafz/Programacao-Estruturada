contador = 1
soma = 0
while True:
    num = int(input(f'Digite o {contador} número: '))
    if num == 0:
        print('Programa encerrado!')
        break
    soma = soma + num
    contador = contador + 1
print(f'Soma: {soma}')    