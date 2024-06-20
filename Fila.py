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