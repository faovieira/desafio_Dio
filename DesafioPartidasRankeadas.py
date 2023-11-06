def calcular_nivel(vitorias, derrotas):
    ranking = vitorias - derrotas

    if ranking <= 10:
        nivel = 'Ferro'
    elif 11 <= ranking <= 20:
        nivel = 'Bronze'
    elif 21 <= ranking <= 50:
        nivel = 'Prata'
    elif 51 <= ranking <= 80:
        nivel = 'Ouro'
    elif 81 <= ranking <= 90:
        nivel = 'Diamante'
    elif 91 <= ranking <= 100:
        nivel = 'Lendário'
    else:
        nivel = 'Imortal'

    return ranking, nivel

vitorias = int(input('Digite o número de vitórias: '))
derrotas = int(input('Digite o número de derrotas: '))

resultado = calcular_nivel(vitorias, derrotas)

print('Se foram {} vitórias e {} derrotas:\nO Herói tem de saldo de {} vitórias e está no nível de {}.'.format(vitorias, derrotas, resultado[0], resultado[1]))