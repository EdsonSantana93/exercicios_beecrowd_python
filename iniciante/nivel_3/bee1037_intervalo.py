def validarIntervalo(valor:float) -> str:
    if valor >= 0 and valor <= 25:
        return '[0,25]'
    elif valor > 25 and valor <= 50:
        return '(25,50]'
    elif valor > 50 and valor <= 75:
        return '(50,75]'
    elif valor > 75 and valor <= 100:
        return '(75,100]'
    return None


entrada = float(input())
intervalo = validarIntervalo(entrada)

if intervalo:
    print(f'Intervalo {intervalo}')
else:
    print('Fora de intervalo')
