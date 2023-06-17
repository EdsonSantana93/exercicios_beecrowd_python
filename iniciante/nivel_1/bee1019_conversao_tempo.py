def converter_hora(segundos: int) -> str:
    minuto, segundo = divmod(segundos, 60)
    hora, minuto = divmod(minuto, 60)
    return f"{hora}:{minuto}:{segundo}"


segundos = int(input())
print(converter_hora(segundos))
