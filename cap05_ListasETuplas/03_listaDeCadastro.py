from os import system, name

system("cls") if name == "nt" else system("clear")
run = ""
listaDeNomes = []
listaDeTelefones = []
while run != "X":
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    listaDeNomes.append(nome)
    listaDeTelefones.append(telefone)
    run = input("Digite qualquer tecla para continuar.Para encerrar digite 'X'. ").upper()
for i in range(len(listaDeNomes)):
    print(f"Nome: {listaDeNomes[i]} - Tel: {listaDeTelefones[i]}")
