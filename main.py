from Torre import torre
from Apartamento import apartamento
from fila import fila

listaTorres = []
listaAps = []

#Instânciando, cadastrando Torres e imprimindo lista de torres
t1 = torre(listaTorres, "Amarelo", "Rua Abcdef")
t1.cadastrar(listaTorres)
t2 = torre(listaTorres, "Verde", "Rua Fghijk")
t2.cadastrar(listaTorres)
t3 = torre(listaTorres, "Rosa", "Rua Lmnopqrs")
t3.cadastrar(listaTorres)
torre.imprimirLista(listaTorres)

#Instânciando e cadastrando apartamentos
ap1 = apartamento(1, 202, t1, 8)
ap1.cadastrar(listaAps)
ap2 = apartamento(5, 302, t2)
ap2.cadastrar(listaAps)
ap3 = apartamento(8, 202, t3)
ap3.cadastrar(listaAps)
ap4 = apartamento(77, 201, t1)
ap4.cadastrar(listaAps)
ap5 = apartamento(13, 301, t3)
ap5.cadastrar(listaAps)
ap6 = apartamento(13, 202, t2)
ap6.cadastrar(listaAps)

#Instânciando a fila e adicionando 3 apartamentos a escolher no Terminal
f1 = fila()
f1.adicionar(listaAps)
f1.adicionar(listaAps)
f1.adicionar(listaAps)

#imprimindo a fila
f1.imprimir()

#excluindo o primeiro apartamento da fila e atribuindo a vaga ocupada
f1.excluir(15)

#imprimindo a fila
f1.imprimir()

#imprimindo a lista de apartametnos
apartamento.imprimirListaAp(listaAps, listaTorres)

