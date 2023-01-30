from os import system, name

system("cls") if name == "nt" else system("clear")


def soma(x, y):
    try:
        print("Soma: ", (float(x) + float(y)))
    except:
        print("Ocorreu um erro!")


def subtrai(x, y):
    try:
        print("Subtração: ", (float(x) - float(y)))
    except:
        print("Ocorreu um erro!")


def multiplica(x, y):
    try:
        print("Multiplicação: ", (float(x) * float(y)))
    except:
        print("Ocorreu um erro!")


def divide(x, y):
    try:
        print("Divisão: {:.2f}".format((float(x) / float(y))))
    except ZeroDivisionError as erro:
        print(erro)
    except:
        print("Ocorreu um erro!")


run = ""
while run != "X":
    numX = input("Insira o primeiro número: ")
    numY = input("Insira o segundo número: ")
    operador = float(input("Escolha uma opção de cálculo:\n"
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
