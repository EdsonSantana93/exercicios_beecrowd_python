valores = []
numeros_impares = []

for _ in range(2):
    valores.append(int(input()))

for numero in range(min(valores) + 1, max(valores)):
    if numero % 2 == 1:
        numeros_impares.append(numero)
        
print(sum(numeros_impares))
