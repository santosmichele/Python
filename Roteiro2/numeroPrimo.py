###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

primo = int(input())

listaPrimos = (2, 3, 5,7,11)
while primo != -1:
    ehPrimo = 1
    for i in range(5):
        if (primo % listaPrimos[i] == 0) and (primo not in listaPrimos) or (primo == 1):
            ehPrimo = 0
    print (ehPrimo)
    primo = int(input())
        
