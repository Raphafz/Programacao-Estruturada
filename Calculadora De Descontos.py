#CALCULADORA DE DESCONTO

# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida

'''
2.  Calculadora de desconto (você dá o preço e a % de desconto e o programa te retorna o valor com desconto)

'''

print('=====================================\n')
print('BEM VINDO A CALCULADORA DE DESCONTO!\n')
print('=====================================')
preco = float(input('Insira o preço do produto: '))
desconto = int(input('Insira a porcentagem do desconto(%): '))
novo = preco - (preco * desconto/ 100)
print('====================================')
print(f'O produto custava {preco}R$\n')
print('-----------------------------------')
print(f'Com desconto de {desconto}%\n') 
print('-----------------------------------')
print(f'Vai custar {novo:.2f}R$\n')
print('=====================================')