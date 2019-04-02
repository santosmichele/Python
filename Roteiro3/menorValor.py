###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

numeroElementos = int(input())
listaElementos = input()
listaElementos = listaElementos.split(" ", numeroElementos)

print("Menor valor: %i\nPosicao: %i" % (int(min(listaElementos)), int(listaElementos.index(min(listaElementos)))) )