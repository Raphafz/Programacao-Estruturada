# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida



'''
14. Criar uma lista de alunos, ir adicionando os nomes a essa lista
e quando o usuário digitar “fim” ele encerra e mostra a lista de
alunos.

'''



alunos = []

for nomes in range(1,20):
    nomes = input('Escreva os nomes dos alunos: ')
    if nomes == 'fim': 
        print(alunos)
        
    alunos.append(nomes)
    
        
       

