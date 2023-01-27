from os import system
system("cls")

print("Vamos calcular a raiz quadrada.")
numero = input("Informe um número: ")
print("O valor é um número inteiro? ", numero.isnumeric())
print("O valor é um decimal?", numero.isdecimal())
raiz = int(numero) ** (1/2)

print("A raiz quadrada de {} é {:.2f}".format(numero, raiz))
