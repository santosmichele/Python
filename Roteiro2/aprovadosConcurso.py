###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

totalQuestoesPort = 50
totalQuestoesMat = 35
aprovados = 0
notaPortugues = int(input())

while notaPortugues > 0:
    notaMatematica = int(input())
    notaRedacao = float(input())
    if ( (notaPortugues >= (0.8*totalQuestoesPort)) and (notaMatematica >= (0.6*totalQuestoesMat) and notaRedacao >= 7) ):
        aprovados += 1
    notaPortugues = int(input())
print (aprovados)