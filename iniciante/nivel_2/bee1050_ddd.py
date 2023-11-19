def carregar_ddd():
    data = {
        '61': 'Brasilia',
        '71': 'Salvador',
        '11': 'Sao Paulo',
        '21': 'Rio de Janeiro',
        '32': 'Juiz de Fora',
        '19': 'Campinas',
        '27': 'Vitoria',
        '31': 'Belo Horizonte'
    }
    return data 


ddds = carregar_ddd()
ddd_informado = input()
ddd_encontrado = ddds.get(ddd_informado, 'DDD nao cadastrado')

print(f'{ddd_encontrado}')
