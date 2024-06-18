"""3. Código para Gerar a Sequência de Fibonacci"""
def fibonacci(n):
    sequencia = [0, 1]
    while len(sequencia) < n:
        prox_numero = sequencia[-1] + sequencia[-2]
        sequencia.append(prox_numero)
    return sequencia

n = int(input('Digite quantos numeros da sequencia deseja ver:'))
resultado = fibonacci(n)
print(resultado)
