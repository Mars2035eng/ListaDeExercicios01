class apartamento:

    def __init__(self, ident, numero, torre, vaga=None):
        self.id = ident
        self.numero = numero
        self.torre = torre
        self.vaga = vaga
        self.proximo = None

    def cadastrar(self, lista):
        lista.append(self)

    def imprimirAp(self):
        print("-----APARTAMENTO-----")
        print("ID: ", self.id, "\nNúmero: ", self.numero, "\nTorre: ", self.torre.nome, "\nVaga de garagem: ", self.vaga)

    @staticmethod
    def imprimirListaAp(listaAP, listaT):
        x = input("Imprimir apartamentos por torre (T) ou por Número (N)? (S) para sair: ")

        if x.upper() == "T":
            for i in listaT:
                print("\n------ TORRE:", i.nome, "-------")
                for p in listaAP:
                    if p.torre.nome == i.nome:
                        print("Id: ", p.id, "-  AP: ", p.numero, "-  VAGAS: ", p.vaga)

        elif x.upper() == "N":
            listaAux = []
            for i in listaAP:
                a = str(i.numero) + i.torre.nome
                listaAux.append(a)
            listaAux_ordem = sorted(listaAux)

            print("\n-----LISTA DE APARTAMETNOS------")
            for i in listaAux_ordem:
                for p in listaAP:
                    if i == str(p.numero) + p.torre.nome:
                        print("AP: ", p.numero, "  -  TORRE: ", p.torre.nome, "-  VAGA: ", p.vaga)

        elif x.upper() == "S":
            pass

        else:
            print("Escolha uma opção válida")
            return apartamento.imprimirListaAp(listaAP, listaT)

    @staticmethod
    def imprimirListaApOrdem(listaAP):
        print("\n-----LISTA DE APARTAMETNOS------")
        for i in listaAP:
            print("Item: ", listaAP.index(i), "-  Número: ", i.numero, "-  Torre: ", i.torre.nome, "-  Vaga de garagem: ", i.vaga)
        print("")
