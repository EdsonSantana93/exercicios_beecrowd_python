def carregando_informacoes_animais() -> dict:
    data = {('vertebrado', 'ave', 'carnivoro'): 'aguia',
            ('vertebrado', 'ave', 'onivoro'): 'pomba',
            ('vertebrado', 'mamifero', 'onivoro'): 'homem',
            ('vertebrado', 'mamifero', 'herbivoro'): 'vaca',
            ('invertebrado', 'inseto', 'hematofago'): 'pulga',
            ('invertebrado', 'inseto', 'herbivoro'): 'lagarta',
            ('invertebrado', 'anelideo', 'hematofago'): 'sanguessuga',
            ('invertebrado', 'anelideo', 'onivoro'): 'minhoca'
    }
    return data


categoria = input()
classe = input()
habitos_alimentares = input()

animais = carregando_informacoes_animais()

animal_encontrado = animais.get((categoria, classe, habitos_alimentares), 'Nenhum animal encontrado')

print(f'{animal_encontrado}')
