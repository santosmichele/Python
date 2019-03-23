###############################################################################################
###################################### Michele Santos #########################################
################################# Algoritimos e Programação I #################################
################################## IFPB - Eng. de Computação ##################################
###############################################################################################

#Caso esse valor seja inferior a 110, o programa deve exibir a mensagem Glicose Normal. Caso seja 200 ou mais,
#  a mensagem exibida deve ser Glicose Muito Alta. Nos demais casos, o programa deve exibir Glicose Alterada.

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