def calcular_total(roupa1, roupa2):
    total_roupa1 = int(roupa1[1]) * float(roupa1[2])
    total_roupa2 = int(roupa2[1]) * float(roupa2[2])
    return total_roupa1 + total_roupa2


roupa1 = input().split(' ')
roupa2 = input().split(' ')

total = calcular_total(roupa1, roupa2)

print(f'VALOR A PAGAR: R$ {total:.2f}')
