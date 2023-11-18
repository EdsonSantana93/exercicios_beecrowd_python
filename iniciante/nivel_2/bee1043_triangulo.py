def validar_se_forma_triangulo(a:float, b:float, c:float) -> bool:
    return (b + c) > a and (b + c) > a and (c + a) > b

def calcula_perimetro(a:float, b:float, c:float) -> float:
    return a + b + c

def calcular_area(a:float, b:float, c:float) -> float:
    return ((a + b) / 2) * c

entrada = input().split()
a, b, c = map(float, entrada)
forma_trangulo = validar_se_forma_triangulo(a, b, c)

if forma_trangulo:
    perimetro = calcula_perimetro(a, b, c)
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = calcular_area(a, b, c)
    print(f"Area = {area:.1f}")
