import math

def validar_tipo_triangulo(A, B, C):
    tipo_triangulos = []
    if A >= B + C:
        tipo_triangulos.append('NAO FORMA TRIANGULO')
    else: 
        if math.pow(A, 2) == (math.pow(B, 2) + math.pow(C, 2)):
            tipo_triangulos.append('TRIANGULO RETANGULO')
        if math.pow(A, 2) > (math.pow(B, 2) + math.pow(C, 2)):
            tipo_triangulos.append('TRIANGULO OBTUSANGULO')
        if math.pow(A, 2) < (math.pow(B, 2) + math.pow(C, 2)):
            tipo_triangulos.append('TRIANGULO ACUTANGULO')
        if A == B == C:
            tipo_triangulos.append('TRIANGULO EQUILATERO')
        if (A == B and C != A) or (A == C and B != A) or (B == C and A != B) :
            tipo_triangulos.append('TRIANGULO ISOSCELES')
    return tipo_triangulos



#Inicio programa
entrada = input().split()
pontos = list(map(float, entrada))

pontos.sort(reverse=True)

tipos_triangulos = validar_tipo_triangulo(*pontos)

print(*tipos_triangulos, sep='\n')