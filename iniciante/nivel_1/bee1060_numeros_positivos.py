numeros = []

for _ in range(6):
    numeros.append(float(input()))
numeros_positivos = list(filter(lambda x: x > 0, numeros))  
quantidade_positivo = len(numeros_positivos)
print(f'{quantidade_positivo} valores positivos')
