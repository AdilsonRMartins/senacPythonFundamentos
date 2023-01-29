from os import system, name

system("cls") if (name == "nt") else system("clear")
print("Multitabuada 1")
for i in range(1, 11):
    print("{: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4}".format(i, i * 2, i * 3, i * 4, i * 5,
                                                                                         i * 6, i * 7, i * 8, i * 8,
                                                                                         i * 10))
print("Multitabuada 2")
for i in range(1, 11):
    linha = "{: >4} ".format(i)
    for ii in range(2, 11):
        linha += "{: >4} ".format(ii * i)
    print("isso" + linha)
