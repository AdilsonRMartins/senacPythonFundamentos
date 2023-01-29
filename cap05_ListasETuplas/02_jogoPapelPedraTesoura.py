from os import system, name
import random

system("cls") if name == "nt" else system("clear")

run = "S"
while run == "S":
    system("cls") if name == "nt" else system("clear")
    print("*** Jogo Pedra Papel Tesoura ***")
    computador = random.randint(0, 2)
    jogador = int(input("Qual a sua jogada?:\n"
                        "[0] Pedra\n"
                        "[1] Papel\n"
                        "[2] Tesoura\n"
                        "Digite sua escolha: "))
    pecas = ("Pedra", "Papel", "tesoura")
    print(f"Você escolheu: {pecas[jogador]}")
    print(f"O computador escolheu: {pecas[computador]}")
    resultados = ((0, 1, -1), (-1, 0, 1), (1, -1, 0))
    jogada = resultados[computador][jogador]
    if jogada == 0:
        final = "Empate."
    elif jogada == -1:
        final = "Vitória do computador."
    else:
        final = "Vitória do jogador."
    print(f"Resultado: {final}")
    run = input("Digite 'S' para jogar novamente. Ou, qualquer tecla para encerrar: ").upper()

