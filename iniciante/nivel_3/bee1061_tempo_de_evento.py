from datetime import datetime

dia_inicio = int(input()[4:])
horario_inicio = input().split(' : ')
hora_inicio, minuto_inicio, segundo_inicio = map(int, horario_inicio)

data_inicial = datetime(2000, 4, dia_inicio, hora_inicio, minuto_inicio, segundo_inicio)

dia_final = int(input()[4:])
horario_final = input().split(' : ')
hora_final, minuto_final, segundo_final = map(int, horario_final)

data_final = datetime(2000, 4, dia_final, hora_final, minuto_final, segundo_final)

tempo_do_evento = data_final - data_inicial
dias = tempo_do_evento.days

horario_em_segundos = tempo_do_evento.seconds
horas = int(horario_em_segundos / 3600)
minutos = int((horario_em_segundos % 3600) / 60)
segundos = (horario_em_segundos % 3600) % 60

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')