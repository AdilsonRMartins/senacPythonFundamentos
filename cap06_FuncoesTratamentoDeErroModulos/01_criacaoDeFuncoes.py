from os import system, name

system("cls") if name == "nt" else system("clear")


def soma(x, y):
    print("Soma: ", (int(x) + int(y)))


def subtrai(x, y):
    print("Subtração: ", (int(x) - int(y)))


def multiplica(x, y):
    print("Multiplicação: ", (int(x) * int(y)))


def divide(x, y):
    if int(y) != 0:
        print("Divisão: {:.2f}".format((int(x) / int(y))))
    else:
        print("A operação não é possível!")


run = ""
while run != "X":
    numX = input("Insira o primeiro número: ")
    numY = input("Insira o segundo número: ")
    operador = int(input("Escolha uma opção de cálculo:\n"
                         "1. Soma\n"
                         "2. Subtração\n"
                         "3. Multiplicação\n"
                         "4. Divisão\n"
                         "Digite o número correspondente da sua opção: "))
    if operador == 1:
        soma(numX, numY)
    elif operador == 2:
        subtrai(numX, numY)
    elif operador == 3:
        multiplica(numX, numY)
    else:
        divide(numX, numY)
    run = input("Para encerrar digite 'X'. Ou, qualquer tecla para continuar.").upper()
