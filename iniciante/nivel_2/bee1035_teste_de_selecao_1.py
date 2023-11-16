entrada = input().split()
A, B, C, D = map(int, entrada)
soma_A_B = A + B    
soma_C_D = C + D
C_D_positivos = C > 0 and D > 0
A_par = A % 2 == 0

if C_D_positivos and (B > C and D > A) and soma_C_D > soma_A_B and A_par:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')