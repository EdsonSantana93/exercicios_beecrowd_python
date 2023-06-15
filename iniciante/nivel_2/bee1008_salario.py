def calcular_salario(horas, valor_hora):
    return horas * valor_hora


numero = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())
salario = calcular_salario(horas_trabalhadas, valor_hora)
print(f'NUMBER = {numero}')
print(f'SALARY = U$ {salario:.2f}')
