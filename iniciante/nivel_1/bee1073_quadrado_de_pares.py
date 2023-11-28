import math

limite = int(input())

for numero in range(2, limite + 1, 2):
    quadrado = int(math.pow(numero, 2))
    print(f'{numero}^2 = {quadrado}')
