def verifica_maior(valores):
    a = int(valores[0])
    b = int(valores[1])
    c = int(valores[2])
    maiorAB = int((a + b + abs(a - b)) / 2)
    return maiorAB if maiorAB > c else c


valores = input().split(' ')
maior = verifica_maior(valores)
print(f'{maior} eh o maior')
