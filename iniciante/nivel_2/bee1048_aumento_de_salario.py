def buscar_procentagem_aumento(salario_atual:float) -> float:
    if salario_atual <= 400.00:
        return 15
    elif salario_atual <= 800.00:
        return 12
    elif salario_atual <= 1200.00:
        return 10
    elif salario_atual <= 2000:
        return 7
    return 4


def calcular_salario_novo(salario_atual:float) -> [float, float, float]:
    percentual_aumento = buscar_procentagem_aumento(salario_atual)
    valor_aumento = salario_atual * (percentual_aumento / 100)
    novo_salario = salario_atual + valor_aumento
    return percentual_aumento, valor_aumento, novo_salario


#inicio programa
salario = float(input())
percentual_aumento, valor_aumento, novo_salario = calcular_salario_novo(salario)

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {valor_aumento:.2f}')
print(f'Em percentual: {percentual_aumento} %')
