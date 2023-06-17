valor_lido = int(input())
valor_restante = valor_lido
notas = [100, 50, 20, 10, 5, 2, 1]

print(valor_lido)

for nota in notas:
    quantidade_notas = 0
    if valor_restante >= nota:
        quantidade_notas += valor_restante // nota
        valor_restante -= quantidade_notas * nota
    print(f"{quantidade_notas} nota(s) de R$ {nota},00")
