def calcular_volume(raio):
    pi = 3.14159
    return (4.0/3) * pi * pow(raio, 3)


raio = int(input())
volume = calcular_volume(raio)
print(f'VOLUME = {volume:.3f}')
