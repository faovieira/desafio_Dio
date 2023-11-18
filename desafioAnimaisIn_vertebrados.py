caracteristicas = """Escolha 3 opções: 

vertebrado ou inverterbrado 
ave ou mamifero
inseto ou anelideo
carnivoro ou onivoro
hematofogo ou herbivoro\n"""
print(caracteristicas)

# Dicionário com as relações entre os tipos de animais e suas características
animais = {
    'vertebrado': {
        'ave': {
            'carnivoro': 'aguia',
            'onivoro': 'pomba'
        },
        'mamifero': {
            'onivoro': 'homem',
            'herbivoro': 'vaca'
        }
    },
    'invertebrado': {
        'inseto': {
            'hematofago': 'pulga',
            'herbivoro': 'lagarta'
        },
        'anelideo': {
            'hematofago': 'sanguessuga',
            'onivoro': 'minhoca'
        }
    }
}

a = input('Digite: ')
b = input('Digite: ')
c = input('Digite: ')

# Verifica se as entradas existem no dicionário e retorna o animal correspondente
if a in animais and b in animais[a] and c in animais[a][b]:
    animal = animais[a][b][c]
    print(animal)
else:
    print("Combinação de características de animal não encontrada.")