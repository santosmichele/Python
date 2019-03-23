###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

numeroDesejado = int(input())
inicial = int(input())
final = int(input())
multiplos = []


for x in range(inicial+1, final+1):
    if (x % numeroDesejado == 0):
        multiplos.append(x)
if multiplos == []:
    print("INEXISTENTE")        
else:
    for key, value in enumerate(multiplos):
        print ("%i" %value)