def validar_quadrante(ponto1:float, ponto2:float) -> str:
    if ponto1 == 0.0 or ponto2 == 0.0:
        return validar_quadrante_zero(ponto1, ponto2)
    else:
        return validar_quadrante_sem_zero(ponto1, ponto2)

def validar_quadrante_zero(ponto1: float, ponto2: float) -> str:
    if ponto1 == 0.0 and ponto2 == 0.0:
        return "Origem"
    elif ponto1 == 0.0 and ponto2 != ponto1:
        return "Eixo Y"
    return "Eixo X"

def validar_quadrante_sem_zero(ponto1: float, ponto2: float) -> str:
    if ponto1 > 0.0 and ponto2 > 0.0:
        return "Q1"
    elif ponto1 < 0.0 and ponto2 > 0.00:
        return "Q2"
    elif ponto1 <= 0.0 and ponto2 < 0.00:
        return "Q3"
    return "Q4"


pontos = input().split()

quadrante = validar_quadrante(*map(float, pontos))

print(quadrante)
