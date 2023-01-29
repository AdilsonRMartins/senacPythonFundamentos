from os import system, name

system("cls") if name == "nt" else system("clear")
print("Verificador de Números Primos")
numero = int(input("Informe um número: "))
i = 2
divisor = 0
tipo = "deve ser maior que 2"
while i < numero:
    tipo = "é primo"
    x = numero % i
    if x == 0:
        divisor = i
        tipo = "não é primo"
        break
    i = i + 1
print(f"O número {tipo}.")
print(f"O menor divisor é: {divisor}" if divisor > 0 else "")
