
def validar_se_multiplo(valor1:int, valor2:int) -> bool:
    if valor1 > valor2:
        return valor1 % valor2 == 0
    return valor2 % valor1 == 0 

entrada = input().split()
valor1, valor2 = map(int, entrada)

multiplo = validar_se_multiplo(valor1, valor2)

if multiplo:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
