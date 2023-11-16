import math


def calcular_delta(a, b, c): 
    return math.pow(b,2.0) - 4 * a * c

def calcularX(a, b, delta, operacao):
    try:
        raiz = math.sqrt(delta)
        expoente = None
        resultado = None
        b =  b * (-1) if b > 0  else b

        if operacao == '+':
            expoente = None if raiz == None else  b + raiz
        else:
            expoente = None if raiz == None else b - raiz
        
        resultado = expoente / (2 * a)
        return resultado
    except:
        return None


entrada = input().split()
a, b, c = map(float, entrada)

delta = calcular_delta(a, b, c)

r1 = calcularX(a, b, delta, "+")
r2 = calcularX(a, b, delta, "-")

if r1 or r2: 
    print(f"R1 = {r1:.5f}") 
    print(f"R2 = {r2:.5f}")    
else:
    print("Impossivel calcular")