from random import randint

l = "=" * 70
cont = 0
restul = opcao = ""

print(f"\n\033[1;031m{l}")
print("{: ^70}".format("Jogo do Par ou Ímpar"))
print(l, "\033[m")

while restul == opcao:
    print("\n")
    computador = randint(0, 10)
    opcao = str(input("Quer Par ou Ímpar [P / I]? ")).strip().upper()
    while opcao != "P" and opcao != "I":
        opcao = str(input("Quer Par ou Ímpar [P / I]? ")).strip().upper()
    jogador = int(input("Digite um número de 0 a 10: "))
    while jogador >10:
        jogador = int(input("Digite um número de 0 a 10: "))
    soma = computador + jogador

    if soma % 2 == 0:
        restul = "P"
    else:
        restul = "I"

    print(f"\nO jogador escolheu {opcao} e o número {jogador} e o computador escolheu o número {computador}.")
    print(f"A soma dos dois números foi {soma}, que é um número {restul}\n")

    if restul == opcao:
        print(f"\033[1;033m{l}")
        print("{: ^70}".format("O jogador venceu!! Parabéns!! =D"))
        print(l, "\033[m")
        cont += 1
    else:
        print(f"\033[1;31m{l}")
        print("{: ^70}".format("O computador venceu. Game Over!!  =/"))
        print(l, "\033[m")

print(f"\nO jogador conseguiu {cont} vitórias.")
