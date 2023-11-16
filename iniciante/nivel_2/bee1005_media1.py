PESO_A = 3.5
PESO_B = 7.5

nota_a = float(input())
nota_b = float(input())

soma_media = (nota_a * PESO_A + nota_b * PESO_B)
media = soma_media / (PESO_A + PESO_B)

print(f'MEDIA = {media:.5f}')
