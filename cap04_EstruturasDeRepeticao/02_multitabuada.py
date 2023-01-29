from os import system, name

system("cls") if (name == "nt") else system("clear")

for i in range(1, 11):
    print("{: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4}".format(i, i * 2, i * 3, i * 4, i * 5,
                                                                                         i * 6, i * 7, i * 8, i * 8,
                                                                                         i * 10))
