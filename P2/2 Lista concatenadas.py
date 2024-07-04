# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida

'''
4. Concatenar Duas Listas: Escreva um programa que concatene
duas listas fornecidas pelo usuário.
'''

sair = False
lista1 = []
lista2 = []
while not sair:
    entrada = int(input('''
Selecione uma opção:
  - [1] Adicionar na lista 1
  - [2] Adicionar na lista 2
  - [3] Ver lista
  - [4] Sair \n 
= '''))
    
    if entrada == 1:
        add = input('Adicionar cliente na fila: ')
        lista1.append(add)
        
    if entrada == 2:
        add = input('Adicionar cliente na fila: ')
        lista2.append(add)
        
    if entrada == 3:
        print(lista1 + lista2)

    if entrada == 4:
        sair = True
