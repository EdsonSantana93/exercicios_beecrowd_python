numero = int(input())

numeros_impares = []

while len(numeros_impares) < 6:
    if numero % 2 == 1:
        numeros_impares.append(numero)
    numero += 1   
print(*numeros_impares, sep='\n')
