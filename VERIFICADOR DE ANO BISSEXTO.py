#VERIFICADOR DE ANO BISSEXTO

# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida

'''
7. Verificador de ano bissexto (digita um ano e diz se é ou não)
'''
print('='*50)
print('Bem vindo ao verificador de ano bissexto!')
print('='*50)
ano = int(input('Digite o ano que vai ser verificado: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é um ano bissexto!')
