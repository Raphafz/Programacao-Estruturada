# VERIFICADOR DE INDICE DE MASSA (IMC)

# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida


'''  
1. Calculadora do IMC (usa peso e altura, fórmula é peso / (altura x altura) 
e me diga em qual faixa do IMC a pessoa está Magra, Saudavel, sobrepeso, Obesa ou Muito obesa
'''



print('===================================')
print('Seja bem vindo a calculadora de IMC')
print('===================================')
nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')
peso = float(input('Digite seu peso por favor: '))
altura = int(input('Digite sua altura em centimetros por favor: '))
altura = altura/100
imc = float(peso/(altura*altura))
if imc < 18.5:
    print(f'{nome} Você está muito magro, procure um médico!')
elif imc <= 24.9:
    print(f'{nome} Você está saudável, parabéns!')
elif imc <= 29.9:
    print(f'{nome} Você está sobrepeso, procure um médico!')
elif imc <= 39.9: 
    print(f'{nome} Você está obeso, procure um médico!')
else:
    print(f'{nome} Você está muito obeso, procure um médico URGENTE!!!!')
