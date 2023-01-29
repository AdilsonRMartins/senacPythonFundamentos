from os import system, name

system("cls") if name == "nt" else system("clear")

num = int(input("Digite um número entre 0 e 99: "))

numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove")
dez = ("dez", "onze", "doze", "treze", "quatorze", "quinze", "dezeseis", "dezessete", "dezoito", "dezenove")
dezenas = ("", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "noventa")

if num < 10:
    extenso = numeros[num]
elif num < 20:
    extenso = dez[num - 10]
elif num <= 99:
    dezena = int(num / 10)
    numeral = num % 10
    complemento = ""
    if numeral != 0:
        complemento = " e "
    extenso = dezenas[dezena] + complemento + numeros[numeral]
else:
    extenso = "Não digitou um número válido."
print(extenso)
