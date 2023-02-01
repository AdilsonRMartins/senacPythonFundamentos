import io
import sys
import os
import zipfile
import urllib.request as request

BUFF_SIZE = 1024


def download(resposta, saida):
    total_downloaded = 0
    while True:
        data = resposta.read(BUFF_SIZE)
        total_downloaded += len(data)
        if not data:
            break
        saida.write(data)
    print("Tamanho do arquivo {bytes}".format(bytes=total_downloaded))


def zip(path):
    if not os.path.exists(path):
        print("Arquivo {} não existe".format(path))
        sys.exit(-1)
    else:
        arquivoZip = zipfile.ZipFile(path)
        arquivoZip.extractall()
        print("Arquivos extraídos")


url = "https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_win32.zip"
resposta = request.urlopen(url)
pasta = os.path.abspath(os.getcwd())
arquivoSaida = io.FileIO(f"{pasta}\chromedriver_win32.zip", mode="w")
download(resposta, arquivoSaida)
zip(f"{pasta}\chromedriver_win32.zip")
print(f"Download realizado na página {url}")
