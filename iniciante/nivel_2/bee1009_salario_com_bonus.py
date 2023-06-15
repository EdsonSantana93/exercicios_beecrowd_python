def calcular_comissao(valor_vendas):
    return valor_vendas * 0.15


def calcular_salario(salario_base, valor_vendas):
    return salario_base + calcular_comissao(valor_vendas)


nome = input()
salario_base = float(input())
valor_vendas = float(input())
salario_total = calcular_salario(salario_base, valor_vendas)
print(f'TOTAL = R$ {salario_total:.2f}')
