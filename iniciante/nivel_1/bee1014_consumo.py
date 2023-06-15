def calcular_consumo(distancia, combustivel_gasto):
    return distancia / combustivel_gasto


distancia = int(input())
combustivel_gasto = float(input())
consumo = calcular_consumo(distancia, combustivel_gasto)
print(f'{consumo:.3f} km/l')
