import math
from os import system, name

system("cls") if name == "nt" else system("clear")
help(math)
print("math.ceil de 4.2:", math.ceil(4.2))
print("math.floor de 3.9:", math.floor(3.9))
print("math.fabs - valor absoluto de -1:", math.fabs(-1))
print("math.fmod - resto da divisão entre 9 e 4:", math.fmod(9, 4))
print("math.sqrt - raiz quadrada de 36:", math.sqrt(36))
print("round - arredondamento de 9.988 com uma casa decimal", round(9.988, 1))
