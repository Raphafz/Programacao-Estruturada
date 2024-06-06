contador = 1
soma = 0
while contador <= 10:
    num = int(input(f'Digite o {contador} número: '))
    soma = soma + num
    contador = contador + 1
print(f'Soma: {soma}')