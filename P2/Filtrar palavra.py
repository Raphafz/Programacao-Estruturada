# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida



'''
16. Filtrar Palavras de uma Lista
Objetivo: Escrever um programa que percorre uma lista de palavras e
imprime apenas as palavras que começam com uma determinada letra
fornecida pelo usuário.
Descrição:
O programa solicita ao usuário uma letra.
Percorre uma lista de palavras.
Imprime apenas as palavras que começam com a letra fornecida.

'''

nomes = ['joão Victor' , 'Vitor', 'Robervaldo', 'Jubiscleito', 'Joel', 'LeBron', 'Pedro', 'Beatriz','Raphael', 'Marcelo']


letra = str(input("Qual a letra desejada ? "))
letra = letra.upper()
if letra:
    filtrar = list(filter(lambda nome: nome.startswith(letra), nomes))
    print (filtrar)
else:
    print ("Digite uma letra para funcionar")