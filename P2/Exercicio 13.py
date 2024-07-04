# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida

'''
13. Digitar numeros para serem somados e quando o usuário
digitar '0' o programa fecha e da o resultado da soma de todos os
numeros digitados.

'''

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