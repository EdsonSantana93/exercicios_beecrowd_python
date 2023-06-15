def calcular_area(raio):
    pi = 3.14159
    return pi * pow(raio, 2)


raio = float(input())
area = calcular_area(raio)
print(f'A={area:.4f}')
