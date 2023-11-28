casos = int(input())
quantidade_no_intervalo = 0
quantidade_fora_intervalo = 0

for _ in range(casos):
    numero_informado = int(input())
    if (numero_informado >= 10 and numero_informado <= 20):
        quantidade_no_intervalo += 1 
    else:
        quantidade_fora_intervalo += 1

print(f'{quantidade_no_intervalo} in')
print(f'{quantidade_fora_intervalo} out')
