from requests import get
from bs4 import BeautifulSoup
from os import system, name

system("cls") if name == "nt" else system("clear")
url = "https://www.imdb.com/search/title/?release_date=2020-01-01,2020-12-31&sort=user_rating,desc"
resposta = get(url)
textoPuro = BeautifulSoup(resposta.text, "html.parser")
filmes = textoPuro.findAll("div", class_="lister-item mode-advanced")
print(len(filmes))
for i in range(10):
    filmesItem = filmes[i]
    nome = filmesItem.h3.a.text
    lancamento = filmesItem.h3.find("span", class_="lister-item-year text-muted unbold")
    votos = filmesItem.find("span", attrs={"name": "nv"})
    nomeEpisodio = filmesItem.h3.find('small', 'text-primary unbold')
    episodio = ""
    if episodio is not None:
        ep = filmesItem.find_all('a')
        episodio = "- Episódio: " + ep[2].text + ","
    print("{}. {} {} {}\nVotos: {} - Pontuação: {}\n".format(i + 1, nome, episodio, lancamento.text, votos.text,
                                                           filmesItem.strong.text))
