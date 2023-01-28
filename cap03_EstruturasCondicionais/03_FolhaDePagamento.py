from os import system, name

system("cls") if (name == "nt") else system("clear")

print("Folha de Pagamento")
salario = float(input("Informe o valor do salário: "))

if (salario > 6433.23):
    inss = 900.70
elif (salario >= 3305.23):
    inss = salario * 0.14
elif (salario >= 2203.49):
    inss = salario * 0.12
elif (salario >= 1100.01):
    inss = salario * 0.09
else:
    inss = salario * 0.075

base = salario - inss
if (base > 4664.68):
    aliquota = 0.275
    deducao = 869.36
elif (base >= 3751.06):
    aliquota = 0.225
    deducao = 636.13
elif (base >= 2826.66):
    aliquota = 0.15
    deducao = 354.80
elif (base >= 1903.99):
    aliquota = 0.075
    deducao = 142.80
else:
    aliquota = 0
    deducao = 0

ir = (aliquota * base) - deducao
salarioLiquido = base - ir

print("Salário Bruto: {:.2f}\n"
      "Salário Base: {:.2f}\n"
      "INSS: {:.2f}\n"
      "%IR: {:.2f}\n"
      "Valor do IR: {}\n"
      "Salário Líquido: {:.2f}".format(salario, base, inss, aliquota * 100, ir, salarioLiquido))
