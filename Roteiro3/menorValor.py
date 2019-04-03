###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

numeroElementos = int(input())
listaElementos = input()
listaElementos = listaElementos.split(" ", numeroElementos)
for i in range(len(listaElementos)):
    listaElementos[i] = int(listaElementos[i])

print("Menor valor: %i\nPosicao: %i" % (int(min(listaElementos)), int(listaElementos.index(min(listaElementos)))) )