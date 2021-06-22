class torre:

    def __init__(self, lista, nome, endereco):
        self.id = len(lista) + 1
        self.nome = nome
        self.endereco = endereco

    def cadastrar(self, lista):
        lista.append(self)

    def imprimirTorre(self):
        print(self.id, " - ", self.nome, " - ", self.endereco)

    @staticmethod
    def imprimirLista(lista):
        i = 1
        print("--------LISTA DE TORRES-------")
        for x in lista:
            print(i, "- Torre", x.nome, "-  Endereço: ", x.endereco)
            i += 1

    def getNome(self):
        return self.nome

    def getEndereco(self):
        return self.endereco

    def getId(self):
        return self.id

    def setNome(self, nome):
        self.nome = nome

    def setEndereco(self, endereco):
        self.endereco = endereco
