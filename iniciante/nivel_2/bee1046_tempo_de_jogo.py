def calcular_tempo_jogo(inicio, fim):
    if inicio > fim:
        return 24 - inicio + fim
    elif inicio < fim:
        return fim - inicio
    return 24

entrada = input().split()
inicio_fim = map(int, entrada)
tempo_jogo = calcular_tempo_jogo(*inicio_fim)
print(f'O JOGO DUROU {tempo_jogo} HORA(S)')
