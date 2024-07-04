# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida


'''
7. Adicionar Elementos a uma Lista com append: Escreva um
programa que solicite ao usuário para adicionar elementos a uma
lista até que ele digite "parar". Em seguida, exiba a lista completa.
'''


item = 0
lista = []
while True:
    item = str(input(f"Qual o item deseja adicionar na lista ? Digite 'Parar' para parar o codigo \n" "Apenas Letras : \n"))
    if item == "Parar":
        print ("Fim da lista")
        break
    lista.append (item)
print (f"{lista}")