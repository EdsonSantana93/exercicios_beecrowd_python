def calcular_area_triangulo(base, altura):
    return base * altura / 2


def calcular_area_circulo(raio):
    pi = 3.14159
    return pi * pow(raio, 2)


def calcular_area_trapezio(altura, *base):
    return ((base[0] + base[1]) * altura) / 2


def calcular_area_quadrado(base):
    return pow(base, 2)


def calcular_area_retangulo(base, altura):
    return base * altura


medidas = input().split(' ')
a = float(medidas[0])
b = float(medidas[1])
c = float(medidas[2])
triangulo = calcular_area_triangulo(a, c)
circulo = calcular_area_circulo(c)
trapezio = calcular_area_trapezio(c, a, b)
quadrado = calcular_area_quadrado(b)
retangulo = calcular_area_retangulo(a, b)

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')
