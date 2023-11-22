numeros = []

for _ in range(5):
    numeros.append(int(input()))
quantidade_pares = len(list(filter(lambda x: x % 2 == 0, numeros)))
quantidade_impares = len(list(filter(lambda x: x % 2 == 1, numeros)))
quantidade_positivo = len(list(filter(lambda x: x > 0, numeros)))
quantidade_negativo = len(list(filter(lambda x: x < 0, numeros)))
print(f'{quantidade_pares} valor(es) par(es)')
print(f'{quantidade_impares} valor(es) impar(es)')
print(f'{quantidade_positivo} valor(es) positivo(s)')
print(f'{quantidade_negativo} valor(es) negativo(s)')
