# VERIFICADOR DE NUMEROS 

# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida
'''
10. Um programa que verifique se um número é Positivo e par, positivo e múltiplo
    de três, negativo e ímpar, Zero ou se não é nenhum desses.
'''


print('=============================================')
print('''Bem vindo ao verificador de números!\n
 Vamos verificar se o número é:
    -Positivo e par
    -Positivo e múltiplo de 3
    -Negativo e ímpar
    -Se o número é zero      
''')
print('=============================================')
numero = float(input('Digite o número que será verificado: '))
if numero % 2 == 0 and numero > 0:
    print('O número é par e positivo')
elif numero > 0 and numero % 3 == 0:
    print('O número é Positivo e múltiplo de 3')
elif numero % 2 == 1 and numero < 0:
    print('O número é ímpar e negativo')
elif numero == 0:
    print('O número é zero')
else:
    print('O número não é nunhuma das alternativas!')
