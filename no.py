from Apartamento import apartamento


class no:

    def __init__(self, lista):

        apartamento.imprimirListaApOrdem(lista)
        a = input("Selecione o númeor do item AP para incluir na fila de vagas: ")
        if int(a) < len(lista):
            self.ap = lista[int(a)]
            self.proximo = None

        else:
            print("Apartamento não incluído, escolha um valor válido")
            self.ap = None
            self.proximo = None
