# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida



'''
10. Números Perfeitos: Um número perfeito é um número inteiro
positivo que é igual à soma de seus divisores próprios (excluindo
ele mesmo). Escreva um programa que verifica se um número é
perfeito.
'''



n = int(input("Digite o valor de n: "))
soma = 0
  
for divisor in range(1,n):
     if n % divisor == 0:
        soma += divisor 
if n == soma:
    print(f"O numero {n} é perfeito")
else: 
    print(f"O numero {n} nao é perfeito\n")
  