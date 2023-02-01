from requests import get
from bs4 import BeautifulSoup
from os import system, name

system("cls") if name == "nt" else system("clear")
url = "https://chromedriver.chromium.org/downloads"
resposta = get(url)
print(resposta.status_code)
html = BeautifulSoup(resposta.content, "html.parser")
tags = html.find_all("ul")
for i in range(len(tags)):
    if (tags[i].text.find("you are using Chrome version") > 0):
        listas = tags[i].findAll("li")
        if len(listas) >= 1:
            print(listas[1].text)
            print(listas[1].text[-12:])
            urlDownload = "https://chromedriver.storage.googleapis.com/" + listas[1].text[
                                                                           -12:] + "/chromedriver_win32.zip"
            print(urlDownload)
