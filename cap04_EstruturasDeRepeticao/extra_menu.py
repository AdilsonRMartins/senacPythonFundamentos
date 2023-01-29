from os import system, name

system("cls") if name == "nt" else system("clear")
run = ""
while run != "X":
    print("Sistema funcionando...")
    run = input("Digite:\n"
                "X para sair, ou qualquer tecla para continuar: ").upper()
    system("cls") if name == "nt" else system("clear")
