from decimal import Decimal, ROUND_HALF_UP

valor_lido = Decimal(input())
valor_restante = valor_lido
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.10, 0.05, 0.01]


def contar_notas_moedas(tipo_moeda: str, lista_moeda: list,
                        valor_restante: float) -> float:
    print(f'{tipo_moeda.upper()}S:')
    for item in lista_moeda:
        item = Decimal(item)
        item = item.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
        quantidade_notas_moeda = 0
        if valor_restante >= item:
            quantidade_notas_moeda += int(valor_restante // item)
            valor_restante -= quantidade_notas_moeda * item
        print(f"{quantidade_notas_moeda} {tipo_moeda}(s) de R$ {item:.2f}")
    return valor_restante


valor_restante = contar_notas_moedas('nota', notas, valor_restante)
contar_notas_moedas('moeda', moedas, valor_restante)
