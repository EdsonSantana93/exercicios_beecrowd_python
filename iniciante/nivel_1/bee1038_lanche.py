def calcular_total(valor_lanche:float, quantidade_lanche:float) -> float:
    return valor_lanche * quantidade_lanche

lanche = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}

entrada = input().split()
lanche_escolhido, quantidade_lanche = map(int, entrada)
valor_lanche = lanche[lanche_escolhido]

valor_total = calcular_total(valor_lanche, quantidade_lanche)

print(f'Total: R$ {valor_total:.2f}')
