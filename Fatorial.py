num = int(input("Fatorial de: ") )

resultado = 1
for n in range(1,num + 1):
    resultado *= n

print(f'O resultado: {resultado}')
