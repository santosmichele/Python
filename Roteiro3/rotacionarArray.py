###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

tamanhoLista = int(input())
lista = list()
for i in range(tamanhoLista):
    lista.append(int(input()))
deslocamento = int(input())
novaLista = list()
for i in range(deslocamento, tamanhoLista):
    novaLista.append(lista[i])
for i in range(0, deslocamento):
    novaLista.append(lista[i])

for i in range(len(novaLista)):
    print(novaLista[i])

