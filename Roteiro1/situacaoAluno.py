###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################
notas = []
mediaAritimetica = 0

for x in range(0,3):
    notas.append(int(input()))
    mediaAritimetica +=notas[x]

mediaAritimetica = mediaAritimetica/len(notas)
status = ""
mensagem = ""

if ( mediaAritimetica >= 70 and mediaAritimetica <= 100):
    status = "APROVADO"
elif ( mediaAritimetica >= 40 and mediaAritimetica < 70):
    status = "FINAL"
elif ( mediaAritimetica >= 0 and mediaAritimetica < 40):
    status = "REPROVADO"

if (mediaAritimetica < 0 or mediaAritimetica > 100):
    print ("Media invalida")
else:
    print ("A media do aluno foi %.2f e ele foi %s" %(mediaAritimetica, status))
