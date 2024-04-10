# Conversor de  de comprimento

# Aluno: Raphael Ferraz
# Curso: Técnico de Informtica 
# Matéria: Programção Estruturada
# Professor: Matheus Almeida

'''
9. Um programa que faz  conversão do valor que o usuário digitar em (Milhas,
Polegadas, Pés, Centímetros, Metros ou Quilômetros) para todos os outros de
acordo com o que o usuário escolher primeiro.
'''

print('Bem vindo o Conversor de medidas de comprimento\n')
print('========== Unidades de medidas  ===========\n')
print(''' 
    1.Milhas (mi)
    2.Centímetro (cm)
    3.Pés (pe)  
    4.Polegadas(Pol)
    5.Metros (M)
    6.Quilômetro (km) 
     ''')
print('='*41)
escolha = input('Escolha um opção: ')
if escolha == '1':
    mi = float(input('Digite o número em milhas: '))
    km = mi *  1.6093
    m = mi * 1609
    cm = mi * 160900
    pe = mi * 5280
    pol = mi * 63360
    print(f'{mi} milhas são {km} Quilômetros \n')
    print(f'{mi} milhas são {m} Metros \n')
    print(f'{mi} milhas são {cm} centímetros\n')
    print(f'{mi} milhas são {pe} pés \n')
    print(f'{mi} milhas são {pol} polegadas\n')
    print('ALGUMAS MEDIDAS SÃO APROXIMADAS!!!!!(≈)')
elif escolha == '2':
    cm = float(input('Digite o número em centímetros: '))
    km = cm / 100000
    m = cm / 100
    mi = cm / 160900
    pe = cm / 30.48
    pol = cm / 2.54 
    print(f'{cm} centímetros são {km} Quilômetros\n')
    print(f'{cm} centímetros são {m} metros\n')
    print(f'{cm} centímetros são {mi} milhas\n')
    print(f'{cm} centímetros são {pe} pés\n')
    print(f'{cm} centímetros são {pol} polegadas\n')
    print('ALGUMAS MEDIDAS SÃO APROXIMADAS!!!!!(≈)')
elif escolha == '3':
    pe = float(input('Digite o número em pés: '))
    km = pe / 3281
    m = pe / 3.281
    mi = pe / 5280
    cm = pe * 30.48
    pol = pe * 12
    print(f'{pe} pés são {km} Quilômetros \n')
    print(f'{pe} pés são {m} metros \n')
    print(f'{pe} pés são {mi} milhas \n')
    print(f'{pe} pés são {cm} centímetro \n')
    print(f'{pe} pés são {pol} polegadas \n')
    print('ALGUMAS MEDIDAS SÃO APROXIMADAS!!!!!(≈)')
elif escolha == '4':
    pol = float(input('Digite o número em polegadas: '))
    km = pol / 39370
    m = pol / 39.37
    mi = pol / 63360
    cm = pol * 2.54
    pe = pol / 12
    print(f'{pol} polegadas são {km} Quilômetros  \n')
    print(f'{pol} polegadas são {m:} metros  \n')
    print(f'{pol} polegadas são {mi} milhas \n')
    print(f'{pol} polegadas são {cm} centímetro \n')
    print(f'{pol} polegadas são {pe} pés  \n')
    print('ALGUMAS MEDIDAS SÃO APROXIMADAS!!!!!(≈)')
elif escolha == '5':
    m = float(input('Digite o número em metros: \n'))
    km = m / 1000
    pol = m * 39.37
    mi = m / 1609
    cm = m * 100
    pe = m * 3.281
    print(f'{m} metros são {km} Quilômetros \n')
    print(f'{m} metros são {pol} polegadas  \n')
    print(f'{m} metros são {mi} milhas  \n')
    print(f'{m} metros são {cm} centímetro  \n')
    print(f'{m} metros são {pe} pés \n')
    print('ALGUMAS MEDIDAS SÃO APROXIMADAS!!!!!(≈)')
elif escolha == '6':
    km = float(input('Digite o número em Quilômetros: '))
    m = km * 1000
    pol = km * 39370
    mi = km / 1.609
    cm = km * 100000
    pe = km * 3281
    print(f'{km} Quilômetros são {m} metros \n')
    print(f'{km} Quilômetros são {pol} polegadas  \n')
    print(f'{km} Quilômetros são {mi} milhas  \n')
    print(f'{km} Quilômetros são {cm} centímetro \n')
    print(f'{km} Quilômetros são {pe} pés \n')
    print('ALGUMAS MEDIDAS SÃO APROXIMADAS!!!!!(≈)')
else:
    print('Opção inválida, tente novamente!\n')



