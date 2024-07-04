# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida

'''
8. Pedir 10 números para o usuário e no final retornar a soma dos 10
números.
'''


contador = 1
soma = 0
while contador <= 10:
    num = int(input(f'Digite o {contador} número: '))
    soma = soma + num
    contador = contador + 1
print(f'Soma: {soma}')