###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

totalNotas = int(input())

if (totalNotas < 1 or totalNotas > 5):
    print ("Numero de notas invalido.")
else:
    notas = list()
    for i in range(totalNotas):
        notas.append(float(input()))
    for j in range(totalNotas):
        print ("Nota %d: %.1f" %((j+1), notas[j]) )
    print ("Media: %.2f" %float((sum(notas))/totalNotas))

