#Vericador de numeros primos

# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida


print('Bem Vindo ao verificador de números primos!')


Num = int(input('Digite um número: '))
primo = 0
for i in range(1,Num + 1):
        if Num % i == 0:
            primo += 1
if primo == 2: 
    print(f'{Num}, É um número primo!')
else: 
    print(f'{Num}, Não é um número primo!')
