###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

diaAnterior = 0
conseguiu = -1
totalPoupado = 0

for i in range(7):
    valorDepositado=float(input())
    if ( (valorDepositado-0.5) >= diaAnterior):
        conseguiu += 1
    diaAnterior = valorDepositado
    totalPoupado += valorDepositado
print ("R$ %.2f\n%i" %(totalPoupado,conseguiu))