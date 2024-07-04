# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida

'''
15.
comidas = ['leite', 'couve','computador', 'tomate','garfo','faca','tablet','refrigerante']
bebidas = ['uva', 'colher','TV','vinho','cerveja','celular','banana']
talheres = ['arroz','iPhone', 'concha','whisky','vodka','feijão','colher de chá']

criar uma nova lista para eletrônicos e adicionar os eletrônicos a
ela e organizar as demais listas

'''


comidas = ['leite', 'couve','computador', 'tomate','garfo','faca','tablet','refrigerante']
bebidas = ['uva', 'colher','TV','vinho','cerveja','celular','banana']
talheres = ['arroz','iPhone', 'concha','whisky','vodka','feijão','colher de chá']
eletronicos = []

comidas.remove ('leite')
comidas.remove ('garfo')
comidas.remove ('faca')
comidas.remove ('refrigerante')
comidas.remove ('computador')
comidas.remove ('tablet')

bebidas.remove ('uva')
bebidas.remove ('colher')
bebidas.remove ('banana')
bebidas.remove ('TV')
bebidas.remove ('celular')

talheres.remove ('arroz')
talheres.remove ('whisky')
talheres.remove ('vodka')
talheres.remove ('feijão')
talheres.remove ('iPhone')

comidas.extend (['uva', 'banana', 'arroz', 'feijao'])
bebidas.extend (['refrigerante', 'whisky', 'vodka', 'leite'])
talheres.extend (['garfo', 'faca', 'colher'])
eletronicos.extend (['computado', 'tablet', 'TV', 'celular', 'iPhone'] )

print('=-'*40)
print (f'A lista de comidas é {comidas}')
print('=-'*40)
print (f'A lista de bebidas é {bebidas}')
print('=-'*40)
print (f'A lista de talheres é {talheres}')
print('=-'*40)
print (f'A lista de eletronicos é {eletronicos}')
print('=-'*40)