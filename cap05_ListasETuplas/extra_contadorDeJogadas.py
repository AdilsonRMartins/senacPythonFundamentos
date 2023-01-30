from os import system, name
import random

system("cls") if name == "nt" else system("clear")

run = "S"
empate = 0
vitoriasComputador = 0
vitoriasUsuario = 0
while run == "S":
    print("*** Jogo Pedra Papel Tesoura ***")
    computador = random.randint(0, 2)
    jogador = int(input("Qual a sua jogada?:\n"
                        "[0] Pedra\n"
                        "[1] Papel\n"
                        "[2] Tesoura\n"
                        "Digite sua escolha: \n"))
    pecas = ("Pedra", "Papel", "tesoura")
    print(f"Você escolheu: {pecas[jogador]}")
    print(f"O computador escolheu: {pecas[computador]}")
    resultados = ((0, 1, -1), (-1, 0, 1), (1, -1, 0))
    jogada = resultados[computador][jogador]

    if jogada == 0:
        final = "Empate."
        empate+= 1
    elif jogada == -1:
        final = "Vitória do computador."
        vitoriasComputador+= 1
    else:
        final = "Vitória do jogador."
        vitoriasUsuario+= 1
    print(f"Resultado: {final}")
    print("\nHistórico de jogadas:")
    print(f"Empates: {empate}.\n"
          f"Vitórias do usuário: {vitoriasUsuario}.\n"
          f"Vitórias do computador: {vitoriasComputador}.\n")
    run = input("Digite 'S' para jogar novamente. Ou, qualquer tecla para encerrar: ").upper()
