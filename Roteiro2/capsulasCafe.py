###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

contador = 0

for i in range(7):
    quantidade = int(input())
    tamanhoCaixa = input()
    
    if tamanhoCaixa.upper() == 'P':
        contador += 10*quantidade
    elif tamanhoCaixa.upper() == 'G':
        contador += 16*quantidade
print ("%d\n%d" %(contador, (contador*2)/7 )  )