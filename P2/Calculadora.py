# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida

'''
9. Criação de uma Calculadora: Escreva um programa que
implemente uma calculadora simples que pode realizar as quatro
operações básicas: soma, subtração, multiplicação e divisão.
'''


num1 = float (input("Escolha um numero : "))
operador = str (input("Escolha um operador : '+ - * /' : "))
num2 = float (input("Escolha outro numero : "))
if operador == "+":
    print('=-'*20)
    print (f"O resultado é = {num1 + num2}")
    print('=-'*20)
elif operador == "-":
    print('=-'*20)
    print (f"O resultado é = {num1 - num2}")
    print('=-'*20)
elif operador == "*":
    print('=-'*20)
    print (f"O resultado é = {num1 * num2}")
    print('=-'*20)
elif operador == "/":
    print('=-'*20)
    print (f"O resultado é =  {num1 / num2}")
    print('=-'*20)
else:
    print ("Entrada invalida!!!")
