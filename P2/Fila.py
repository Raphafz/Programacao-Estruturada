# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida


'''
1. Gerenciar uma Fila de Atendimento
Objetivo: Simule uma fila de atendimento onde novos clientes são
adicionados ao final da lista e os clientes atendidos são removidos
do início da lista.

'''



sair = False
fila = []

while not sair:
    entrada = int(input('''
Selecione uma opção:
  - [1] Adicionar
  - [2] Remover
  - [3] Ver Fila
  - [4] Sair \n 
= '''))
    
    if entrada == 1:
        add = input('Adicionar cliente na fila: ')
        fila.append(add)
        
    if entrada == 2:
        remove = input('Cliente removido!!!!(APERTE ENTER PARA CONTINUAR)')
        fila.pop(0)
        
    if entrada == 3:
        print(fila)

    if entrada == 4:
        sair = True