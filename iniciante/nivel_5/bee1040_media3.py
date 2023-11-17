import decimal

def calcular_media(notas:list) -> float:
    peso_prova = [2.0, 3.0, 4.0, 1.0]
    media = 0
    for i in range(len(notas)):
        media += decimal.Decimal(notas[i]) * (decimal.Decimal(peso_prova[i]) 
                                              / decimal.Decimal(10.0))
    media = media.quantize(decimal.Decimal('0.0'), rounding=decimal.ROUND_DOWN)
    return float(media)

def calcular_media_exame(media:float, prova_exame:float) -> float:
    media_final = ((decimal.Decimal(media) + decimal.Decimal(prova_exame)) / 2)
    media_final = media_final.quantize(decimal.Decimal('0.0'), 
                                       rounding=decimal.ROUND_DOWN)
    return media_final

def validar_aprovacao(media:float) -> str:
    if media >= 7.0:
        return 'Aluno aprovado.'
    elif media < 5.0:
        return 'Aluno reprovado.'
    return 'Aluno em exame.'

def valida_aprovacao_exame(media:float) -> str:
    if media >= 5.0:
        return 'Aluno aprovado.'
    return 'Aluno reprovado.'


# Inicio do programa
entrada = input().split()
notas = list(map(float, entrada))
media = calcular_media(notas)
aprovacao = validar_aprovacao(media)

print(f'Media: {media:.1f}')
print(aprovacao)

if aprovacao == 'Aluno em exame.':
    prova_exame = float(input())
    print(f'Nota do exame: {prova_exame:.1f}')
    media_exame = calcular_media_exame(media, prova_exame)
    aprovacao_exame = valida_aprovacao_exame(media_exame)

    print(aprovacao_exame)
    print(f'Media final: {media_exame:.1f}')
