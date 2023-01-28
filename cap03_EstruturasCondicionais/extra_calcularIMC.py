from os import system, name

system("cls") if (name == "nt") else (system("clear"))
print("Calcuradora de IMC")
peso = float(input("Informe o seu peso eh Kg: "))
altura = float(input("Agora, informe a sua altura em m: "))
imc = peso / (altura * altura)
print("O seu IMC é: {:.2f}".format(imc))
if imc >= 40:
    classificacao = "Obesidade Grau III ou Mórbida"
elif imc >= 35:
    classificacao = "Obesidade Grau II"
elif imc >= 30:
    classificacao = "Obesidade Grau I"
elif imc >= 25:
    classificacao = "Sobrepeso"
elif imc >= 18.5:
    classificacao = "Peso normal"
else:
    classificacao = "Abaixo do peso"
print("A sua classificação é: {}".format(classificacao))
