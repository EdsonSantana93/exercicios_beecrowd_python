import math


def calcular_distancia(*planos):
    resultado_plano_x = pow((float(planos[1][0]) - float(planos[0][0])), 2)
    resultado_plano_y = pow((float(planos[1][1]) - float(planos[0][1])), 2)
    parcial = resultado_plano_x + resultado_plano_y
    return math.sqrt(parcial)


ponto_1 = input().split(' ')
ponto_2 = input().split(' ')
distancia = calcular_distancia(ponto_1, ponto_2)

print(f'{distancia:.4f}')
