from no import no


class fila:

    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def adicionar(self, lista):

        if self.tamanho == 0:
            a = no(lista)
            if a.ap != None:
                self.inicio = a
                self.tamanho += 1

        else:
            aux = self.inicio
            while aux.proximo:
                aux = aux.proximo

            a = no(lista)
            if a.ap != None:
                aux.proximo = a
                self.tamanho += 1

    def excluir(self, vaga):

        if self.tamanho == 0:
            print("A fila está vazia")

        else:
            if self.inicio.ap.vaga == None:
                self.inicio.ap.vaga = str(vaga)
            else:
                self.inicio.ap.vaga = str(self.inicio.ap.vaga), vaga
                self.inicio = self.inicio.proximo
            print("Item exluído com sucesso")

    def imprimir(self):

        if self.tamanho == 0:
            print("A fila está vazia")

        else:
            i = 1
            aux = self.inicio
            print("----FILA DE ESPERA-----")
            while aux:
                print(i, " - AP: ", aux.ap.numero, " - TORRE", aux.ap.torre.nome)
                i += 1
                aux = aux.proximo
