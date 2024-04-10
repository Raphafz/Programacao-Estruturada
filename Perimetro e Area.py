#CALCULO DO PERIMETRO E AREA DE UM RETANGULO

# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida

'''
4. Cálculo do perímetro e área de um retângulo
'''

print('='*47)
print('Calculadora de área e perimetro de um retângulo')
print('='*47)

base = float(input('Digite a base do retângulo em CM: '))
altura = float(input('Digite a altura do retângulo em CM: '))
area = base * altura
perimetro = 2 *(base + altura)
print(f'A área do retângulo é: {area} CM, e o perimetro é: {perimetro} CM')