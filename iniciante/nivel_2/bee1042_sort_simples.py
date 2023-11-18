entrada = input().split()
numeros = list(map(int, entrada))
numeros_iniciais = numeros.copy()

numeros.sort(reverse=False)

print(*numeros, sep='\n', end='\n\n')

print(*numeros_iniciais, sep='\n')
