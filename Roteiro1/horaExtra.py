###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################
salarioBase = float(input())
horasExtras = float(input())
valorHora = (salarioBase/44) 
valorHora = valorHora + (valorHora*(10/100))
salarioFinal = (valorHora*horasExtras) + salarioBase
print ("%.2f" %salarioFinal)