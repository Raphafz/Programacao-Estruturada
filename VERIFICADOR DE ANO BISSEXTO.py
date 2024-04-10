#VERIFICADOR DE ANO BISSEXTO

# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida

'''
7. Verificador de ano bissexto (digita um ano e diz se é ou não)
'''
print('='*50)
print('Bem vindo ao Verificador de ano bissexto!')
print('='*50)
ano = int(input('Digite um Ano: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'{ano} é um ano Bissexto!')
else:
    print(f'{ano} Não é um ano bissexto!')