from os import system
system("cls")

print("Conversor de Medidas")
medida = float(input("Informe uma medida em centímetros: "))
print("Para qual nidade de medida deseja converter?")
print("Digite: 1 - Polegadas | 2 - Pés | 3 - Jardas")
opcao = input("Opção: ")
if opcao == "1":
    polegadas = medida / 2.54
    print("{} centímetros representam {:.4f} polegadas.".format(medida,polegadas))
elif opcao == "2":
    pes = medida / 30.48
    print("{} centímetros representam {:.4f} pés.".format(medida,pes))
elif opcao == "3":
    jardas = medida / 91.44
    print("{} centímetros representam {:.4f} jardas.".format(medida, jardas))
else:
    print("Opção inválida.")