from os import system, name

system("cls") if (name == "nt") else (system("clear"))

print("Tabuada Simples")
multiplicador = int(input("Informe o multiplicador: "))
for i in range(1, 11):
    print("{} * {} = {}".format(multiplicador, i, multiplicador * i))
