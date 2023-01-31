import os.path, datetime
from os import system, name

system("cls") if name == "nt" else system("clear")
arquivo = "produtos.csv"
if os.path.isfile(arquivo):
    produtos = open(arquivo, "r", encoding="utf-8")
    tamanho = os.path.getsize(arquivo)
    modificacao = os.path.getmtime(arquivo)
    print("Data de modificação:", datetime.datetime.fromtimestamp(modificacao))
    print("Tamanho do arquivo (bytes):", tamanho)
    listaDeProdutos = []
    for line in produtos:
        colunas = line.strip().split(";")
        colunas[0] = int(colunas[0])
        colunas[2] = int(colunas[2])
        colunas[3] = int(colunas[4])
        colunas[4] = int(colunas[5])
        colunas[5] = int(colunas[6])
        colunas[6] = int(colunas[7])
        colunas[8] = float(colunas[8])
        colunas[9] = float(colunas[9])
        listaDeProdutos.append(colunas)
    produtos.close()
    for prod in listaDeProdutos:
        print(prod)
