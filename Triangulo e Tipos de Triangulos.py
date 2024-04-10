#VERIFICAÇÃO DE TRIANGULO E TIPO DE TRIANGULO 

# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida

'''
8. Verificação de triangulo e tipo de triangulo (dizer se com os 3 comprimentos
que você forneceu é possível formar um triangulo) e dizer depois qual e o tipo
do triangulo (equilátero, isósceles e escaleno)
'''
print('='*50)
print('Verificador de triangulo e tipos de triangulos')
print('='*50)
Ld1 = float(input('Digite o primeiro segmento: '))
Ld2 = float(input('Digite o segundo segmento: '))
Ld3 = float(input('Digite o terceiro segmento: '))
if (Ld1 < Ld2 + Ld3) and (Ld2 < Ld1 + Ld3) and (Ld3 < Ld1 + Ld2):
    print('Os segmentos podem formar um triângulo ', end='')
    if Ld1 == Ld2 == Ld3:
        print('Equilátero')
    elif Ld1 != Ld2 != Ld3:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('Os segmentos não podem Formar um Triângulo ')