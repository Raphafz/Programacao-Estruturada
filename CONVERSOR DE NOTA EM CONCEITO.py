#CONVERSOR DE NOTA EM CONCEITO

# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida

# 6. Conversor de nota em conceito (9+=a, 7.5+=b, 6+=c, 4+=d, resto = f)

print('===========================================')
print('Bem vindo ao conversor de notas em conceito')
print('===========================================')

nota=float(input('Digite a sua nota [0.0 - 10.0]: '))

if nota >= 9:
    print('A sua nota é A')
elif nota >= 7.5:
    print('A sua nota é B')
elif nota >= 6:
    print('A sua nota é C')
elif nota > 4:
    print('A sua nota é D')
else:
    print('A sua nota é F')
