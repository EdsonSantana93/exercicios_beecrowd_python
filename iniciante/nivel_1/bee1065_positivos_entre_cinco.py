numeros = []

for _ in range(5):
    numeros.append(int(input()))
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
quantidade_pares = len(numeros_pares)
print(f'{quantidade_pares} valores pares')
