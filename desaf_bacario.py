from time import sleep
print("Bem vindo ao Banco Python.\n...")

menu = ("""
(1) depositar
(2) extrato
(3) sacar
(4) sair
\nEscolha uma das opções acima: """)

sleep(0.5)

saque_por_dia = 3
limite_diario = 500
saldo = 0
extrato = " "
saques = 0

while True:
    opçao = input(menu)

    if opçao == "1" :
        valor = float(input('Digite o valor do depósito: '))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opçao == "3":
        valor = float(input("Informe o valor do saque: "))

        saldo_excedido = valor > saldo

        limite_excedido = valor > limite_diario

        saques_excedidos = saques >= saque_por_dia

        if saldo_excedido:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif limite_excedido:
            print("Operação falhou! O valor do saque excede o limite.")

        elif saques_excedidos:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            saque += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opçao == "2":
        print("\n################ EXTRATO ################")
        print("Conta sem movimentações recentes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opçao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
