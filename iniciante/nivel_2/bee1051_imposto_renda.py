def calcular_valor_pagar_faixa(valor_calculo:float, faixa:float) -> float:
    aliquota = {
        2: 0.08,
        3: 0.18,
        4: 0.28
    }
    
    return valor_calculo * aliquota.get(faixa)

limite_faixa = {
    1: 2000.00,
    2: 3000.00,
    3: 4500.00
}

valor_renda = float(input())
faixa = 1
valor_imposto = 0

if valor_renda > limite_faixa.get(faixa):
    for faixa in range(2, 5):
        valor_faixa_anterior = limite_faixa.get(faixa - 1)
        valor_faixa_atual = limite_faixa.get(faixa)
        valor_restante = valor_renda - valor_faixa_anterior
        if valor_restante <= 0.0:
            break
        valor_maximo_calcular_faixa = valor_faixa_atual - valor_faixa_anterior if valor_faixa_atual else valor_restante
        valor_calculo = min(valor_restante, valor_maximo_calcular_faixa)
        valor_imposto += calcular_valor_pagar_faixa(valor_calculo, faixa)
    print(f'R$ {valor_imposto:.2f}')
else:
    print('Isento')
