###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

temperatura = float (input())
sintomas = input()

if not( (sintomas == 'S' or sintomas == 'N') and (temperatura >=35 and temperatura <=41  ) ):
    print ("Erro")
elif ( temperatura >= 37 and sintomas == 'S' ):
    print ("Exames Especiais")
elif ( (temperatura <= 37 and sintomas == 'S') or  (temperatura >= 37 and sintomas == 'N' ) ):
    print ("Exames Basicos")
else:
    print ("Liberado")