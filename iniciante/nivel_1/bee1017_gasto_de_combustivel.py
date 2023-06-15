def calcular_distancia_percorrida(tempo, velocidade):
    return tempo * velocidade


def calcular_combustivel_gasto(distancia_percorrida):
    return distancia_percorrida / 12


tempo = int(input())
velocidade = int(input())
distancia_percorrida = calcular_distancia_percorrida(tempo, velocidade)
combustivel_gasto = calcular_combustivel_gasto(distancia_percorrida)
print(f'{combustivel_gasto:.3f}')
