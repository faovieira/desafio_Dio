nome = input('Digite o nome do Herói: ')
experiencia = int(input('Digite o número de XP do personagem: '))

if experiencia <= 1000:
    nivel = 'Ferro'
elif 1001 <= experiencia <= 2000:
    nivel = 'Bronze'
elif 2001 <= experiencia <= 6000:
    nivel = 'Prata'
elif 6001 <= experiencia <= 7000:
    nivel = 'Ouro'
elif 7001 <= experiencia <= 8000:
    nivel = 'Platina'
elif 8001 <= experiencia <= 9000:
    nivel = 'Ascendente'
elif 9001 <= experiencia <= 10000:
    nivel = 'Imortal'
else:
    nivel = 'Radiante'

print("O Herói de nome {} está no nível {}".format(nome, nivel))
