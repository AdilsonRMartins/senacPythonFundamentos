from num2words import num2words


class recibo:
    def __init__(self, nome):
        self.nome = nome
        self._valor = 0
        self._descricao = ""

    def __str__(self):
        texto = "Recebemos de {} a quantia de R${} ({})".format(self.nome, self.valor, self.extenso())
        descricao = "\nReferente a {}".format(self.descricao) if (self._descricao != "") else ""
        dados = "{}\n{}{}".format(" Recibo ".center(len(texto), "*"), texto, descricao)
        return dados

    def descricao(self, value):
        self.descricao = value

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, value):
        self._valor = value

    def extenso(self):
        vextenso = num2words(self._valor, lang="pt_BR", to="currency")
        return vextenso
