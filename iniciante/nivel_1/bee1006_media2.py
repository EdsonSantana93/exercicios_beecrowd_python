def calcular_media(*notas):
    soma = 0
    for nota in notas:
        soma += nota

    return soma


A = float(input()) * 0.2
B = float(input()) * 0.3
C = float(input()) * 0.5

media = calcular_media(A, B, C)
print(f'MEDIA = {media:.1f}')
