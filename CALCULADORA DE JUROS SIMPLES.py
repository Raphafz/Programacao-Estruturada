# CALCULADORA DE JUROS SIMPLES

# Aluno: Raphael Ferraz
# Curso: Técnico de Informatica 
# Matéria: Programação Estruturada
# Professor: Matheus Almeida


#5. Calculadora de juros simples (teremos valor principal, taxa de juros e o período)


print('=========================================\n')
print('BEM VINDO A CALCULADORA DE JUROS SIMPLES!\n')
print('=========================================')
vp = float(input('Digite o Valor principal: '))
Juros = int(input('Digite a taxa de juros em %: '))
periodo = int(input('Digite em quantos meses deseja o retorno: '))
Juros = Juros/100 
Taxa_juros = (vp * Juros * periodo)
Valor_final = vp + Taxa_juros
print(f'----- Tempo percorrido {periodo} meses -----')
print(f'Valor do juros da aplicação: {Taxa_juros:.2f}')
print(f'Valor do montante da aplicação: R$ {Valor_final:.2f}')
print(f'---------------------------------------------\n')