def calcular_ano_mes_dia(dias: int) -> list:
    ano, mes = divmod(dias, 365)
    mes, dia = divmod(mes, 30)
    return [ano, mes, dia]


dias = int(input())

tempo = calcular_ano_mes_dia(dias)
print(f'{tempo[0]} ano(s)')
print(f'{tempo[1]} mes(es)')
print(f'{tempo[2]} dia(s)')
