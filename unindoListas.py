###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

itensLista = int(input())
if itensLista < 1:
    print ("Erro - A lista deve ter pelo menos 1 elemento.")
else:
    listaUm = list()
    for i in range(itensLista):
        listaUm.append(input())
    itensLista = int(input())
    if itensLista < 1:
        print ("Erro - A lista deve ter pelo menos 1 elemento.")
    else:
        listaDois = list()
        for i in range(itensLista):
            listaDois.append(input())
        
        #poderia colocar o print direto aqui, mas a variavel deixa mais organizado
        resultado = (" ".join(listaUm) + " " + " ".join(listaDois))
        print (resultado)
