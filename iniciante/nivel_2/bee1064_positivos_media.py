numeros = []

for _ in range(6):
    numeros.append(float(input()))
numeros_positivos = list(filter(lambda x: x > 0, numeros))
quantidade_positivo = len(numeros_positivos)
media_positivo = sum(numeros_positivos) / quantidade_positivo
print(f'{quantidade_positivo} valores positivos')
print(f'{media_positivo:.1f}')
