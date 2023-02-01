from requests import get
from bs4 import BeautifulSoup
from os import system, name

system("cls") if name == "nt" else system("clear")
url = "https://economia.uol.com.br/"
response = get(url)
html = BeautifulSoup(response.text, "html.parser")
secaoDinheiro = html.find_all("a", class_="subtituloGrafico subtituloGraficoValor")

for valor in secaoDinheiro:
    print(valor.text)
