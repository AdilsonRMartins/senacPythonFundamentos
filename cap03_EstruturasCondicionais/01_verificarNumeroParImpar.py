from os import system
system("cls")

numero = int(input("Informe um número: "))
resultado = numero % 2
if resultado == 0:
    resultado = "par"
else:
    resultado = "ímpar"
print("O resultado é {}".format(resultado))
