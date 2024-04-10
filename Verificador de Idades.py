#VERIFICADOR DE IDADE

# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida

'''
3. Verificador de idade criança (-13 anos) adolescente 13 a 17, adulto +18 e idoso
+60

'''
print('='*50)
print('Bem vindo ao verificador de idade!')
print('='*50)
idade = int(input('Digite sua idade sua idade: '))
if idade < 13:
    print('Você é uma criança!')
elif idade >= 13 and idade <= 17:
    print ('Você é um adolescente!')
elif idade >= 18 and idade < 60:
    print('Você é um adulto!')
else:
    print('Você é um idoso!')
print('='*50)
