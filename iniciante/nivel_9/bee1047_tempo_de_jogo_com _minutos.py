def calcular_hora_jogo(hora_inicio:int, minuto_inicio:int, hora_fim:int, minuto_fim:int) -> [int, int]:
    horas = minutos = 0
    if hora_inicio > hora_fim:
        horas = 24 - hora_inicio + hora_fim
    elif hora_inicio < hora_fim:
        horas = hora_fim - hora_inicio
    elif hora_inicio == hora_fim and minuto_fim <= minuto_inicio:
        horas = 24
    else:
        horas = 0

    descontar_hora, minutos = calcular_minutos(minuto_inicio, minuto_fim)

    if descontar_hora:
        horas -= 1
    return horas, minutos


def calcular_minutos(minuto_inicio:int, minuto_fim:int) -> [bool, int]:
    if minuto_inicio <= minuto_fim:
        return False, (minuto_fim - minuto_inicio)
    return True, 60 + (minuto_fim - minuto_inicio)


#inicio programa
entrada = input().split()
informacao_tempo = map(int, entrada)
horas, minutos = calcular_hora_jogo(*informacao_tempo)


print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
