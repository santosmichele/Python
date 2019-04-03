###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

tamanho = int(input())
listaUm = list()
listaDois = list()


for i in range(tamanho):
    listaUm.append(int(input()))

for j in range(tamanho):
    listaDois.append(int(input()))

for i in range (tamanho):
    print ("%d\n%d" %(listaUm[i], listaDois[i]))
