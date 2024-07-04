# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida


'''
6. Encontrar o Maior e o Menor Número em uma Lista: Escreva um
programa que encontre e exiba o maior e o menor número em uma
lista de números fornecida pelo usuário.
'''



numero = []

numero = input("Digite a lista de numero separados por espaço : ") .split()
numero = [float(num) for num in numero]

num_max = max(numero)
num_min = min(numero)

print(f"O maior numero da lista é: {num_max}")
print(f"O menor numero da lista é: {num_min} \n")

print (numero)
