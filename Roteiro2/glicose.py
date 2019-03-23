###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

contador = -1
entrada = -1
glicose = 0

while entrada != 0:
    contador += 1
    entrada = int(input())  
    glicose += entrada
    

glicose = glicose/contador

if (glicose < 110):
    print ("Glicose Normal")
elif (glicose >= 200):
    print ("Glicose Muito Alta")
else:
    print ("Glicose Alterada")