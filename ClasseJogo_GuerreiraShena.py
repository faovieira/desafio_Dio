class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "usou magia"
        elif self.tipo == "guerreiro":
            ataque = "usou espada"
        elif self.tipo == "monge":
            ataque = "usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "usou shuriken"
        else:
            ataque = "usou um ataque desconhecido"

        print(f"O {self.tipo} atacou usando {ataque}")


# Criando um herói
nome_heroi = input("Digite o nome do herói: ")
idade_heroi = int(input("Digite a idade do herói: "))
tipo_heroi = input("Digite o tipo do herói (mago, guerreiro, monge, ninja): ")

heroi = Heroi(nome=nome_heroi, idade=idade_heroi, tipo=tipo_heroi)

# Chamando o método atacar
heroi.atacar()