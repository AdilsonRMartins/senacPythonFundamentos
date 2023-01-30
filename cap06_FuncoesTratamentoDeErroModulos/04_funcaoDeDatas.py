from os import system, name
from datetime import datetime


def calculaIdade(nascimento):
    agora = datetime.today()
    idade = agora.year - dataNascimento.year - ((agora.month, agora.day) <= (dataNascimento.month, dataNascimento.day))
    return abs(idade)


def diasDeVida(nascimento):
    agora = datetime.today()
    dias = (agora - dataNascimento).days
    return dias


system("cls") if name == "nt" else system("clear")
print("***-Testes genéricos-***")
print("Hoje é:", datetime.now())

criarData = datetime(2023, 9, 21)
print(type(criarData))

agora = datetime.now()
print("Definição do formato de saída:", agora.strftime("%d/%m/%Y %H:%M"))

print("")
print("***-Testes de cálculos-***")
dataNascimento = input("Informe a data de seu nascimento no formato dd/mm/aaaa: ")
dataNascimento = datetime.strptime(dataNascimento, "%d/%m/%Y")

print(f"A sua idade é de {calculaIdade(dataNascimento)} anos.")
print(f"Você já viveu {diasDeVida(dataNascimento)} dias.")
